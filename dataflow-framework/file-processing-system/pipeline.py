import yaml
from importlib import import_module
import time
from monitor import Monitor


def run_pipeline(input_path=None, lines=None, processor_objs=None, monitor=None, trace_flag=False):
    print(f"🚀 Running pipeline on: {input_path}")
    if input_path and not lines:
        with open(input_path, 'r') as f:
            lines = [line.strip() for line in f]
    try:
        with open(input_path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Failed to read {input_path}: {e}")
        return

    with open("pipeline.yaml") as f:
        pipeline_config = yaml.safe_load(f)["processors"]

    processors = {}
    for name, import_path in pipeline_config.items():
        if import_path == "end":
            continue
        module_name, class_name = import_path.rsplit(".", 1)
        module = import_module(module_name)
        cls = getattr(module, class_name)
        processors[name] = cls()

    for line in lines:
        print(f"📦 Processing line: {line}")
        current = "start"
        trace = ["start"] if trace_flag else None
        content = line

        while current != "end":
            processor = processors[current]
            try:
                start_time = time.time()
                outputs = list(processor.process([content]))
                print(f"🔁 {current} → {outputs}")
                elapsed = time.time() - start_time
                monitor.record(current, elapsed, error=None)

                # Tracing
                if trace_flag:
                    trace.append(current)

                next_step, content = outputs[0]
                current = next_step
            except Exception as e:
                monitor.record(current, 0, error=str(e))
                break

        if trace_flag:
            monitor.add_trace(trace)
