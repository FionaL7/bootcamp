import sys
from engine.router import RoutingEngine
from engine.loader import load_config, build_pipeline

if __name__ == "__main__":
    config = load_config("pipeline.yaml")
    processors = build_pipeline(config)
    engine = RoutingEngine(config["processors"], processors)

    input_lines = (line for line in sys.stdin)
    for output_line in engine.run(input_lines):
        print(output_line, end="")
