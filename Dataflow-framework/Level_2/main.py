from typing import Iterator
from pipeline import get_pipeline


def read_lines(path: str) -> Iterator[str]:
    with open(path, "r") as file:
        for line in file:
            yield line


def write_output(lines: Iterator[str], output_path: str) -> None:
    with open(output_path, "w") as file:
        for line in lines:
            file.write(line + "\n")


def process_file(input_path: str, output_path: str, mode: str) -> None:
    input_lines = read_lines(input_path)
    pipeline = get_pipeline(mode)

    processed_lines = (pipeline[0](line)
                       for line in input_lines)  # Apply processors
    write_output(processed_lines, output_path)
