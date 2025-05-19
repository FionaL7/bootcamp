import argparse
import requests
import sys
import json
import csv

API_URL = "http://localhost:8000/extract"


def main():
    parser = argparse.ArgumentParser(
        description="Extract metadata from scientific articles.")
    parser.add_argument('--ids', nargs='+', required=True,
                        help="List of PMC/PMID IDs")
    parser.add_argument(
        '--output-format', choices=['json', 'csv'], default='json', help="Output format")
    parser.add_argument('--save-to', required=True,
                        help="File path to save results")
    parser.add_argument('--api-key', required=True, help="Your API key")
    parser.add_argument(
        '--ids-file', help="Path to file containing PMC/PMID IDs (one per line)")
    args = parser.parse_args()

    if args.ids_file:
        with open(args.ids_file, "r") as f:
            ids = [line.strip() for line in f if line.strip()]
    else:
        ids = args.ids

    headers = {"X-API-Key": args.api_key}
    payload = {"ids": ids}

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error: {err}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    data = response.json()

    if args.output_format == "json":
        with open(args.save_to, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    elif args.output_format == "csv":

        with open(args.save_to, "w", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["PMC ID", "Title", "Abstract", "Figure Caption",
                            "Figure URL", "Entity Text", "Entity Type"])
            for article in data:
                for fig in article["figures"]:
                    for entity in fig.get("entities", []):
                        writer.writerow([
                            article.get("id"),
                            article.get("title"),
                            article.get("abstract"),
                            fig.get("caption"),
                            fig.get("url"),
                            entity.get("text"),
                            entity.get("type")
                        ])

    print(
        f"✅ Data saved to {args.save_to} in {args.output_format.upper()} format.")


if __name__ == "__main__":
    main()
