from pipeline.base import linewise_processor


def to_upper(line: str) -> str:
    return line.upper()


ToUpper = linewise_processor(to_upper)
