import os
from dotenv import load_dotenv  # type: ignore

load_dotenv()

API_KEY = os.getenv("API_KEY", "supersecret123")
DATA_SOURCE = os.getenv("DATA_SOURCE", "PMC")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
