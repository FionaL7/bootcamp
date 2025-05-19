import argparse
import yaml
import importlib
from monitor.metrics import Monitor
from dashboard.api import start_dashboard
from config import DASHBOARD_PORT
from utils import timeit


def load_pipeline(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    pipeline = config['processors']
    return pipeline


def build_processors(pipeline):
    instances = {}
    for name, path in pipeline.items():
        if path == 'end':
            instances[name] = None
        else:
            module_path, class_name = path.rsplit('.', 1)
            module = importlib.import_module(module_path)
            cls = getattr(module, class_name)
            instances[name] = cls()

    return instances


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trace', action='store_true',
                        help="Enable tracing of line journey")
    parser.add_argument(
        '--config', type=str, default='pipeline.yaml', help="Path to pipeline YAML file")
    parser.add_argument('--input', type=str, required=True,
                        help="Path to input text file")
    args = parser.parse_args()

    monitor = Monitor()
    start_dashboard(monitor, port=DASHBOARD_PORT)

    pipeline = load_pipeline(args.config)
    processor_objs = build_processors(pipeline)

    for name, next_node in pipeline.items():
        if processor_objs[name] is not None:
            processor_objs[name].next_node = next_node

    def process_line_from_file(file_path):
        with open(file_path, 'r') as f:
            for raw_line in f:
                line = raw_line.strip()
                current = 'start'
                trace = []

                while current != 'end':
                    processor = processor_objs[current]
                    try:
                        func = timeit(processor.process)
                        result, elapsed = func([line])
                        result = list(result)
                        if not result:
                            break

                        next_node, line = result[0]
                        if args.trace:
                            trace.append(current)
                        monitor.log_line(current, elapsed, trace=list(
                            trace) if args.trace else None)

                        current = next_node
                    except Exception as e:
                        monitor.log_error(current, str(e))
                        break

    try:
        process_line_from_file(args.input)
    except KeyboardInterrupt:
        print("Shutting down...")


if __name__ == "__main__":
    main()
