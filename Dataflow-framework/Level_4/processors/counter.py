class LineCounter:
    def __init__(self):
        self.count = 0

    def process(self, stream):
        for line in stream:
            self.count += 1
            yield f"{self.count}: {line}"
