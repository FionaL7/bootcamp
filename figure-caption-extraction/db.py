import os
import sqlite3
import logging
from typing import Dict, Any

data_folder = "data"

if not os.path.exists(data_folder):
    os.makedirs(data_folder)

db_path = os.path.join(data_folder, "metadata.db")
logger = logging.getLogger(__name__)


def initialize_db():
    conn = sqlite3.connect("metadata.db")
    logger.info("Initializing the database...")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pmcid TEXT,
            title TEXT,
            abstract TEXT,
            figure_caption TEXT,
            figure_url TEXT,
            entity_text TEXT,
            entity_type TEXT
        );
    """)
    conn.commit()
    conn.close()


def insert_data(article: Dict[str, Any]) -> None:
    conn = sqlite3.connect("metadata.db")
    cursor = conn.cursor()

    for fig in article.get("figures", []):
        caption = fig.get("caption")
        url = fig.get("url")
        entities = fig.get("entities", [])

        for entity in entities:
            cursor.execute("""
                INSERT INTO articles (pmcid, title, abstract, figure_caption, figure_url, entity_text, entity_type)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (
                article.get("pmcid"),
                article.get("title"),
                article.get("abstract"),
                caption,
                url,
                entity.get("text"),
                entity.get("type")
            ))

    conn.commit()

    conn.close()
