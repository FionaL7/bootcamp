# Dataflow Routing Engine

This project implements a streaming text processor pipeline with a configurable **routing engine**. It processes lines of text through a series of **tagged processors**, where each processor emits tagged outputs routed through a **custom-defined processing graph**.

## Features

- Stream-based processing: `Iterator[str] → Iterator[(tag, str)]`
- Tagged routing using `networkx.DiGraph`
- Support for:
  - Stateless processors (e.g., SnakeCase, UpperCase)
  - Stateful processors (e.g., Counter)
- Configurable via a YAML file
- Fan-in and fan-out support (multiple inputs/outputs for a tag)
- Processing ends when tag `end` is emitted

```yaml
processors:
  start: processors.snake_case.SnakeCaseProcessor
  snake_case: processors.to_upper.ToUpperProcessor
  to_upper: processors.counter.CounterProcessor
  counter: end
```

## Sample Processors

- SnakeCaseProcessor: Converts each line to snake_case.

- ToUpperProcessor: Converts each line to uppercase.

- CounterProcessor: Appends a running count to each line.

## Running the Project

- Option 1: Pipe input via stdin

```bash
PYTHONPATH=. python3 main.py < input.txt
```
