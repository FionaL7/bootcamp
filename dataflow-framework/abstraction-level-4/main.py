from pipeline.runner import load_pipeline, run_pipeline
import sys

if __name__ == "__main__":
    processors = load_pipeline("pipeline.yaml")
    input_lines = (line for line in sys.stdin)
    output_lines = run_pipeline(processors, input_lines)

    for line in output_lines:
        print(line, end="")
