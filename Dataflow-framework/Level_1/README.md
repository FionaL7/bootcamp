# Text Processor CLI

A command-line tool for processing text files with different transformation modes. This tool uses typer for the CLI and supports environment-based configuration using python-dotenv.

## Features

- Refactored to use typer for intuitive CLI commands

- Supports input and output file paths via CLI arguments

- Supports multiple processing modes:

- uppercase: Converts text lines to uppercase

- snakecase: Converts text lines to snake_case

- Loads default configuration values from a .env file

## Usage

```bash
python main.py --input path/to/input.txt --output path/to/output.txt --mode uppercase
```

## Example

```bash
python main.py --input input.txt --output output.txt --mode snakecase
```
