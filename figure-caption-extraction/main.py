import os
import logging
import uvicorn  # type: ignore
from typing import List
from config import LOG_LEVEL
from dotenv import load_dotenv  # type: ignore
from pydantic import BaseModel  # type: ignore
from db import initialize_db, insert_data
from fastapi import FastAPI, Depends, HTTPException   # type: ignore
from fastapi.security.api_key import APIKeyHeader, APIKey  # type: ignore
from api.extractor import fetch_article_data, extract_entity_from_caption  # type: ignore


load_dotenv()
os.makedirs("logs", exist_ok=True)
app = FastAPI()
API_KEY = os.getenv("API_KEY", "supersecret123")
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler("logs/ingestion.log"),
                        logging.StreamHandler()
                    ])
logger = logging.getLogger(__name__)


class PaperRequest(BaseModel):
    ids: List[str]


def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403, detail="Invalid or missing API key")
    return api_key


@app.on_event("startup")
async def startup_event():
    initialize_db()


@app.post("/extract")
def extract_from_ids(request: PaperRequest, api_key: APIKey = Depends(verify_api_key)):
    results = []

    for pmcid in request.ids:
        try:
            data = fetch_article_data(pmcid, source="pmc")
            if data:
                data["pmcid"] = pmcid
                for fig in data["figures"]:
                    caption = fig["caption"]
                    fig["entities"] = extract_entity_from_caption(caption)

                insert_data(data)
            results.append({
                "pmcid": pmcid,
                "title": data["title"],
                "abstract": data["abstract"],
                "figures": data["figures"]
            })

        except Exception as e:
            logger.error(e)
            results.append({
                "pmcid": pmcid,
                "error": str(e)
            })

    return {"results": results}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
