# Streaming Text Processor Pipeline

This project implements a streaming text processing pipeline that transforms input text line-by-line using a series of customizable processors. It supports both stateless and stateful processors, configured using a YAML file.

## ✅ Features

- Stream-based architecture: `Iterator[str] -> Iterator[str]`
- Modular and extensible processor system
- Support for processor configuration and internal state
- YAML-configured pipelines
- Works with standard input/output (no intermediate files required)

## 🔧 How It Works

Processors are defined in the `pipeline.yaml` file like so:

```yaml
pipeline:
  - type: processors.snakecase.to_snakecase
  - type: processors.upper.to_upper
  - type: processors.counter.Counter
```

## Example Processor Behaviors:

- to_snakecase: Converts each line to snake_case.

- to_upper: Converts each line to UPPERCASE.

- Counter: Appends a line count to each line.

## Running the Pipeline

```bash
python main.py < input.txt > output.txt
```

## Adding New Processors

To add your own processor:

- Create a new Python file in the pipeline/ directory.

- Define a class or function that accepts Iterator[str] and returns Iterator[str].

- If reusing a line-by-line processor, use the @linewise decorator from linewise.py.
