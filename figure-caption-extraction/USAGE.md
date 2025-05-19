# PMC Data Extraction System — Usage Scenarios

Welcome! This document shows how to use the PMC Data Extraction System via API and CLI, including batch processing and folder watching.

1. Extract Article Data Using the API
   Send a POST request to the /extract endpoint with your list of PMC IDs.

```bash

curl -X POST "http://localhost:8000/extract" \
  -H "Content-Type: application/json" \
  -H "x-api-key: YOUR_API_KEY" \
  -d '{"ids": ["PMC1234567", "PMC7654321"]}'
```

Replace YOUR_API_KEY with your actual API key.

The response will contain article titles, abstracts, figures, and extracted entities.

2. Use the CLI to Process a Batch of PMC IDs from a File
   You can process a batch of IDs stored in a text file (pmc_ids.txt) where each line is a PMC ID.

```bash

python cli.py --api-key YOUR_API_KEY --input-file pmc_ids.txt
```

This sends the IDs to the API and prints the results.

3. Automatic Folder Watcher for Incoming ID Files
   Place a text file containing PMC IDs (one per line) inside the unprocessed/ folder.

### The system will:

- Detect the new file

- Process the IDs by calling the API

- Move the processed file to processed/

- Save results and logs accordingly

- This is great for batch ingestion jobs without manual CLI commands.

4. Sample PMC IDs for Testing
   Use these PMC IDs to quickly test the system:

PMC8824330
PMC8882363
PMC8866415
PMC8771301
PMC8939492

### Notes

- Make sure the API key is set correctly and used in headers or CLI arguments.

- Log files are saved under logs/ for monitoring ingestion jobs.

- The system supports graceful shutdown and clean exits.
