from typing import Iterator
from pipeline import get_yaml_pipeline


def read_lines(path: str) -> Iterator[str]:
    with open(path, "r") as file:
        for line in file:
            yield line.strip()


def write_output(lines: Iterator[str], output_path: str) -> None:
    with open(output_path, "w") as file:
        for line in lines:
            file.write(line + "\n")


def process_file(input_path: str, output_path: str, config_path: str) -> None:
    input_lines = read_lines(input_path)
    pipeline = get_yaml_pipeline(config_path)

    for processor in pipeline:
        input_lines = map(processor, input_lines)

    write_output(input_lines, output_path)
