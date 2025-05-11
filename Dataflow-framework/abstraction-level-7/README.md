# Real-Time Observability Pipeline

A dynamic, pluggable data processing engine with **live metrics**, **trace visualization**, and **error tracking**, all powered by FastAPI and built to operate like a real production system.

## Features

- Modular processor pipeline defined via `pipeline.yaml`
- Real-time metrics for each processor: count, processing time, errors
- Execution tracing of each line's journey through the pipeline
- In-memory storage of recent traces (last 1000 lines)
- Error logging per processor
- Live FastAPI dashboard served on a separate thread

## Usage

### 1. Define Your Pipeline

Edit `pipeline.yaml` to configure your processors:

```yaml
processors:
  start: processors.snake.SnakeCaseProcessor
  snake_case: processors.upper.ToUpperProcessor
  to_upper: processors.counter.CounterProcessor
  counter: end
```

## Run the Engine

```bash
python main.py --input input.txt --trace
```

- --input: Path to your input .txt file

- --trace: (Optional) Enables tracing per line

## Dashboard Endpoints

FastAPI dashboard is served live at:
**Link:** [http://localhost:8000](http://localhost:8000)

- /stats → Live metrics for each processor

- /trace → Recent trace paths (last 1000 lines)

- /errors → Logged exceptions with processor name and error message

## Example Output

🔹 /trace

```json
[["start"], ["start", "snake_case"], ["start", "snake_case", "to_upper"]]
```

🔹 /stats

```json
{
  "snake_case": { "count": 3, "time": 0.0012, "errors": 0 },
  "to_upper": { "count": 2, "time": 0.0011, "errors": 0 }
}
```
