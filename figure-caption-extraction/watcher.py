import os
import time
import requests
import signal
import sys
import logging
from dotenv import load_dotenv

print("in watcher")
load_dotenv()
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler("logs/ingestion.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)

WATCH_DIR = "./watch/unprocessed"
PROCESSED_DIR = "./watch/processed"
API_URL = "http://localhost:8000/extract"
API_KEY = os.getenv("API_KEY")


def process_file(file_path: str):
    with open(file_path, "r") as f:
        ids = [line.strip() for line in f if line.strip()]
    payload = {"ids": ids}
    headers = {"X-API-Key": API_KEY}

    response = requests.post(API_URL, json=payload, headers=headers)
    response.raise_for_status()
    filename = os.path.splitext(os.path.basename(file_path))[0]
    out_file = os.path.join(
        PROCESSED_DIR, filename + ".json")
    with open(out_file, "w", encoding="utf-8") as out_f:
        out_f.write(response.text)
    logger.info(f"Processed: {file_path} → {out_file} ")


def main():
    os.makedirs(WATCH_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    logger.info(f"Watching folder: {WATCH_DIR}")

    while True:
        for file in os.listdir(WATCH_DIR):
            if file.endswith(".txt"):
                file_path = os.path.join(WATCH_DIR, file)
                try:
                    process_file(file_path)
                    os.remove(file_path)
                except Exception as e:
                    print(f" Failed to process {file}: {e}")
        time.sleep(5)


if __name__ == "__main__":
    main()
