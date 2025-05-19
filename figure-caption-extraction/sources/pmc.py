import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
import os
from typing import Dict, List, Optional

load_dotenv()
API_URL = os.getenv("BIOC_API_URL")


def fetch_from_pmc(pmcid: str) -> Optional[Dict[str, any]]:
    url = API_URL + pmcid + "/unicode"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch article: {response.status_code}")

    root = ET.fromstring(response.text)

    article_data = {
        "title": "",
        "abstract": "",
        "figures": []
    }

    for passage in root.findall(".//passage"):
        infon_type = passage.find("infon[@key='type']")
        if infon_type is not None:

            if infon_type.text == "front":
                article_data["title"] = passage.findtext("text", default="")
            elif infon_type.text == "abstract":
                article_data["abstract"] = passage.findtext("text", default="")
            elif infon_type.text in ["fig_caption", "fig_title_caption"]:
                text = passage.find("text")
                if text is not None and text.text.strip():
                    figure_caption = text.text.strip()

                    figure_url = None
                    for infon in passage.findall("infon"):
                        if infon.attrib.get("key") == "url":
                            figure_url = infon.text
                            break

                    article_data["figures"].append({
                        "caption": figure_caption,
                        "url": figure_url,
                        "entities": []
                    })
    return article_data
