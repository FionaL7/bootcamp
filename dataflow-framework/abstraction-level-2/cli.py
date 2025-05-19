# cli.py
import typer
from main import process_file

app = typer.Typer()


@app.command()
def process(
    input: str = typer.Option(..., "--input", help="Input file path"),
    output: str = typer.Option(..., "--output", help="Output file path"),
    mode: str = typer.Option("uppercase", "--mode",
                             help="Processing mode: uppercase, snakecase")
):
    process_file(input, output, mode)


if __name__ == "__main__":
    app()
