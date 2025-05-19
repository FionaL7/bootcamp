# PMC Data Extraction System

A production-ready system to extract metadata, abstracts, figure captions, and biomedical entities from PMC articles using BioC and PubTator APIs.

Includes:

- FastAPI-based backend with API key protection
- SQLite-based storage
- CLI support
- Directory watcher for batch ingestion
- Dockerized deployment
- Logging & graceful shutdown for long-running jobs

## Features

- Secure API with key-based auth
- Extract data from PMC articles via ID
- Entity extraction from figure captions
- Batch ingestion via watched folder or CLI
- Easy Docker deployment
- SQLite backend
- Logs everything to `logs/ingestion.log`

## Requirements

- Python 3.11+
- Docker (for containerized deployment)

## Installation

```bash

git clone https://github.com/FionaL7/bootcamp.git
cd Figure-Caption-Extraction
pip install -r requirements.txt
```

## Docker

```bash
docker build -t paper-extractor .
docker run -p 8000:8000 -e API_KEY=yourapikey paper-extractor
```

## Authentication

```http
X-API-Key: yourapikey
```
try "supersecret123"

## Test PMC IDs

Use the following PMC IDs to test the system:

- PMC8824330
- PMC8882363
- PMC8866415
- PMC8771301
- PMC8939492

## API Endpoints

#### POST /extract

**Description**: Extracts metadata and entities from the given list of PMC IDs.

**Request Body**:

```json
{
  "ids": ["PMC8866415", "PMC8771301"]
}
```

### Headers:

X-API-Key: yourapikey

### Response:

```json

{
  "results": [
    {
      "pmcid": "PMC8866415",
      "title": "...",
      "abstract": "...",
      "figures": [...]
    },
    ...
  ]
}
```

### 🖥️ CLI Usage

```bash
python3 cli.py --ids PMC8771301 PMC8866415 --output-format yourformat --save-to filename --api-key yourapikey
```

## Directory Watcher

- Drop .txt files containing PMC IDs (one per line) into the watch_dir/unprocessed/ folder.

- Files will be automatically processed and moved to watch_dir/processed/.

## Logs

All logs are saved to:

- logs/ingestion.log

## Extensibility

To add new data sources, create a new file like newsource.py and plug it into the SOURCE_HANDLERS factory. No need to rewrite the system.

```python
SOURCE_HANDLERS = {
    "pmc": fetch_from_pmc,
    # "arxiv": fetch_from_arxiv, etc.
}
```
## Live demo 
You can test the API live at :
[Open FASTApi Docs](http://34.59.246.80:8000/docs)
## 🙋‍♀️ Author

- Created by Fiona Lazarus
- Feel free to use, improve, or reach out!
