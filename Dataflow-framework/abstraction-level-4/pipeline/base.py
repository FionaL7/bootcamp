from typing import Iterator, Callable


class Processor:
    def process(self, stream: Iterator[str]) -> Iterator[str]:
        raise NotImplementedError


def linewise_processor(fn: Callable[[str], str]):
    class LineProcessor(Processor):
        def process(self, stream: Iterator[str]) -> Iterator[str]:
            for line in stream:
                yield fn(line)
    return LineProcessor
