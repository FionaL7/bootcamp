import os
from typing import Dict, List
import xml.etree.ElementTree as ET
from dotenv import load_dotenv  # type: ignore
from sources.pmc import fetch_from_pmc
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

load_dotenv()
API_URL = os.getenv("BIOC_API_URL")

SOURCE_HANDLERS = {
    "pmc": fetch_from_pmc,
    # "arxiv": fetch_from_arxiv, etc.
}


def fetch_article_data(paper_id: str, source: str = "pmc"):
    handler = SOURCE_HANDLERS.get(source.lower())
    if not handler:
        raise ValueError(f"Unsupported source: {source}")
    return handler(paper_id)


tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
model = AutoModelForTokenClassification.from_pretrained(
    "d4data/biomedical-ner-all")

nlp_pipeline = pipeline("ner", model=model, tokenizer=tokenizer,
                        aggregation_strategy="simple")


def extract_entity_from_caption(caption: str) -> List[Dict[str, str]]:

    entities = nlp_pipeline(caption)

    allowed_types = {
        "Gene", "Protein", "Disease", "Chemical", "Sign_symptom", "Clinical_event", "Cell_type",
        "Anatomical_system", "Therapeutic_procedure", "Preventive_procedure" "Pathological_formation",
        "Diagnostic_procedure", "Cancer", "Body_part", "Virus", "DNA", "RNA"
    }
    extracted = []
    for entity in entities:
        if entity['entity_group'] in allowed_types:
            extracted.append({
                "text": entity["word"],
                "type": entity["entity_group"]
            })

    return extracted
