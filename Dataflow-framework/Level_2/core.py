from typing import List
from type import ProcessorFunction


def to_upper(line: str) -> str:
    return line.upper()


def to_snakecase(line: str) -> str:
    return line.strip().replace(" ", "_")
