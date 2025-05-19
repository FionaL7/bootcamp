class SnakeCaseProcessor:
    def process(self, lines):
        for line in lines:
            yield ("to_upper", "_".join(line.strip().split()))
