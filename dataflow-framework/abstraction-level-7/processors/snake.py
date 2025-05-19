class SnakeCaseProcessor:
    def process(self, lines):
        for line in lines:
            yield ("snake_case", "_".join(line.strip().split()))
