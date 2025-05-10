import os
import typer
from dotenv import load_dotenv
from typing import Iterator, Optional

app = typer.Typer()

load_dotenv()
DEFAULT_MODE = os.getenv("MODE", "uppercase")


def read_lines(path: str) -> Iterator[str]:
    with open(path, "r") as file:
        for line in file:
            yield line


def transform(line: str, mode: str) -> str:
    line = line.strip()
    if mode == "uppercase":
        return line.upper()
    elif mode == "lowercase":
        return line.lower()
    elif mode == "snakecase":
        return line.lower().replace(" ", "_")
    elif mode == "titlecase":
        return line.title()


def write_output(lines: Iterator[str], output_path: Optional[str]) -> None:
    if output_path:
        with open(output_path, "w") as file:
            for line in lines:
                file.write(line + "\n")
    else:
        for line in lines:
            print(line)


@app.command()
def process(
    input: str = typer.Option(..., "--input", help="Input file path"),
    output: Optional[str] = typer.Option(
        None, "--output", help="Optional output file path"),
    mode: str = typer.Option(
        DEFAULT_MODE, "--mode", help="Processing mode: uppercase, lowercase, snakecase, titlecase")
):
    try:
        input_lines = read_lines(input)
        processed_lines = (transform(line, mode) for line in input_lines)
        write_output(processed_lines, output)
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)


if __name__ == "__main__":
    app()
