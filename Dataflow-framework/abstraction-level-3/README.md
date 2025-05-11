# Dynamic Configurable Pipeline

This version of the Text Processor CLI introduces full decoupling of the processing logic using a dynamic, configuration-driven pipeline. Users can define their desired processing steps in a YAML config file using Python import paths, making the system highly extensible without modifying the codebase.

## Key Concepts

### Feature Description

- Dynamic Pipeline: Define your processor sequence in pipeline.yaml
- Import Path Loading: Load processor functions at runtime using importlib and dotted paths
- Full Decoupling: No need to modify source code to extend behavior—just update the config

## Configuration File: pipeline.yaml

### This file defines the sequence of processors to apply to each line:

```yaml
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
```

### Each type is a dotted import path to a function that matches the signature:

```python
def processor(line: str) -> str
```

## Usage

```bash
python main.py --input <input_file> --config <pipeline_config.yaml> --output <output_file>
```

### Input File

- hello World!
- placeholder text: line two.
- Placeholder text: line three.

### Configuration (pipeline.yaml):

```yaml
pipeline:
  - type: processors.snake.to_snakecase
  - type: processors.upper.to_uppercase
```

### Command:

```bash
python main.py --input input.txt --config pipeline.yaml
```

### Output:

```nginx
HELLO_WORLD
THIS_IS_FUN
```
