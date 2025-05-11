class ToUpperProcessor:
    def process(self, lines):
        for line in lines:
            yield ("to_upper", line.upper())
