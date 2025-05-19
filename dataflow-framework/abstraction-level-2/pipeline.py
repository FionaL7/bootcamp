from typing import List
from core import to_upper, to_snakecase
from type import ProcessorFunction


def get_pipeline(mode: str) -> List[ProcessorFunction]:
    if mode == "uppercase":
        return [to_upper]
    elif mode == "snakecase":
        return [to_snakecase]

    else:
        return [to_upper]
