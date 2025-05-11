import typer
from main import process_file

app = typer.Typer()


@app.command()
def run(input: str = typer.Option(..., help="Path to the input file"),
        output: str = typer.Option(..., help="Path to the output file"),
        config: str = typer.Option(..., help="Path to the pipeline config file")):
    process_file(input, output, config)


if __name__ == "__main__":
    app()
