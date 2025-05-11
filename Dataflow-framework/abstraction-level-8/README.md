# Folder-Based File Processing Pipeline

A self-running, fault-tolerant file processing system using a folder-based queue design. Supports dynamic, YAML-configured pipelines with real-time monitoring via a FastAPI dashboard.

## How It Works

- Drop a .txt file into watch_dir/unprocessed/.

- The watcher picks it up, moves it to underprocess, and runs it through the pipeline.

- Processed files are moved to processed/.

- Monitor stats are available in real time on http://localhost:8000/stats.

## Pipeline Configuration (pipeline.yaml)

```yaml
processors:
  start: processors.snake.SnakeCaseProcessor
  snake_case: processors.upper.ToUpperProcessor
  to_upper: processors.counter.CounterProcessor
  counter: end
```

## Sample Processor

```python

class ToUpperProcessor:
    def process(self, lines):
        for line in lines:
            yield ("to_upper", line.upper())
```

## Monitor Dashboard

Once the system is running, stats and traces can be accessed via:

- **Link:** [http://localhost:8000/stats](http://localhost:8000/stats) – Processor usage, timings, and error counts.

- **Link:** [http://localhost:8000/trace](http://localhost:8000/trace) – Optional trace history (if enabled).

## Running the System

Make sure your directory structure is set up, then run:

```bash

python main.py --trace
```

You'll see:

```arduino

🌐 Dashboard running at http://localhost:8000
🌀 Watcher thread started.
👀 Watching folder: watch_dir/unprocessed
```

## Error Handling

- If a processor throws an exception, it's logged and processing for that line stops.

- Monitor keeps track of errors per processor.

## Features

- Folder-based processing queue

- Modular processor architecture

- Real-time performance monitoring

- Traceable execution path per line

- Extensible via YAML configuration
