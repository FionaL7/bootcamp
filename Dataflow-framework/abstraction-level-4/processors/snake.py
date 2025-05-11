from pipeline.base import linewise_processor
import re


def to_snakecase(line: str) -> str:
    return re.sub(r"\s+", "_", line.strip().lower())


ToSnakecase = linewise_processor(to_snakecase)
