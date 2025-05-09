from typing import List
from core import to_upper, to_lower, to_snakecase, to_titlecase
from type import ProcessorFunction


def get_pipeline(mode: str) -> List[ProcessorFunction]:
    if mode == "uppercase":
        return [to_upper]
    elif mode == "snakecase":
        return [to_snakecase]
    elif mode == "lowercase":
        return [to_lower]
    elif mode == "titlecase":
        return [to_titlecase]
    else:
        return [to_upper]
