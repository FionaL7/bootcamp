# File Processing Pipeline

A modular, traceable file-processing framework that supports both single-file and folder-watch modes, complete with FastAPI endpoints for live status monitoring.

## Features

- Folder-based processing queue (unprocessed, underprocess, processed)

- Plug-and-play processors using YAML pipeline config

- Dual execution modes: Single-file and Watch mode

- FastAPI dashboard for /stats, /files, /health

- Docker-ready with volume mounts

- Makefile for common operations

## Local Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run in single file mode
python main.py --input somefile.txt

# Run in watch mode
python main.py --watch
```

## 🐳 Docker Setup

Build Docker Image

```bash
docker build -t file-pipeline .
```

### Run in Watch Mode

```bash
docker run -p 8000:8000 -v $(pwd)/watch_dir:/app/watch_dir file-pipeline --watch
```

### Run in Single File Mode

```bash

docker run -v $(pwd)/watch_dir:/app/watch_dir file-pipeline --input watch_dir/unprocessed/input.txt
```

Note: On Windows, replace $(pwd) with %cd% or hardcode the full path if needed.

## Uploading Files

You can drop files into watch_dir/unprocessed/, either:

- Directly (in local mode)

- Via volume-mounted Docker (-v flag)

- Using rsync, curl, or upload via FastAPI (if added)

every few minutes to confirm your service is alive.

## Makefile Commands

### Command Description

- make run - Run locally in watch mode
- make build-docker - Build Docker image
- make run-docker - Run Docker container (watch mode)
- make clean - Delete processed files
- make stats - Print stats from FastAPI
