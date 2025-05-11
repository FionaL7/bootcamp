# Text Processor CLI

This project is a structured CLI tool for processing text files using a customizable processing pipeline. At this level, the codebase is modularized for maintainability and extensibility. Each module has a clearly defined responsibility, and text transformations are composed using a common interface.

## Responsibilities

### Module Purpose

- main.py Handles file I/O, uses the CLI and core processing logic
- cli.py Parses CLI arguments (--input, --output, --mode) using Typer
- core.py Defines processor functions (to_uppercase, to_snakecase)
- pipeline.py Assembles the transformation pipeline based on mode
- types.py Declares a standard function type (ProcessorFn = Callable[[str], str])

## Usage

```bash
python main.py --input path/to/input.txt --output path/to/output.txt --mode snakecase
```

### CLI Options

`--input`- Path to input text file
`--output` - Path to output text file (writes to stdout if omitted)
`--mode`- Processing mode (uppercase, snakecase)

## Example

```bash
python main.py --input input.txt --mode uppercase
```

## Input

hello World!
placeholder text: line two.
Placeholder text: line three.

## Output

```bash
HELLO WORLD!

PLACEHOLDER TEXT: LINE TWO.

PLACEHOLDER TEXT: LINE THREE.
```
