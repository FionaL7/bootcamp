class CounterProcessor:
    def __init__(self):
        self.count = 0

    def process(self, lines):
        for line in lines:
            self.count += 1
            yield ("end", f"{self.count}: {line}")
