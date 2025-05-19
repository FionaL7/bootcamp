class ToUpperProcessor:
    def process(self, lines):
        for line in lines:
            yield ("counter", line.upper())
