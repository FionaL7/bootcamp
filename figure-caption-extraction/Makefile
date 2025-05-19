# Makefile for PMC Data Extraction System

# Variables
APP_NAME=pmc_data_extraction
PYTHON=python3
UVICORN_CMD=uvicorn main:app --host 0.0.0.0 --port 8000
DOCKER_IMAGE=paper-extractor

# Run the API locally
run:
	@echo "Starting FastAPI app..."
	$(PYTHON) -m $(UVICORN_CMD)

# Run with reload (for dev)
dev:
	@echo "Running with auto-reload..."
	uvicorn main:app --reload

# Build Docker image
docker-build:
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE) .

# Run Docker container
docker-run:
	@echo "Running Docker container..."
	docker run -p 8000:8000 $(DOCKER_IMAGE)

# Clean up Docker
docker-clean:
	@echo "Cleaning up dangling Docker stuff..."
	docker system prune -f

# Run ingestion from CLI with test file
ingest-cli:
	@echo "Running CLI ingestion from test_ids.txt..."
	$(PYTHON) cli.py --file test_ids.txt

# Watch folder for new files
watch:
	@echo "Starting folder watcher..."
	$(PYTHON) watcher.py

# Format code with black
format:
	@echo "Formatting code..."
	black .

# Run tests (placeholder if you ever add pytest etc.)
test:
	@echo "Running tests..."
	pytest tests/

# Lint (optional, if you use flake8 or ruff)
lint:
	@echo "Linting code..."
	ruff .

.PHONY: run dev docker-build docker-run docker-clean ingest-cli watch format test lint
