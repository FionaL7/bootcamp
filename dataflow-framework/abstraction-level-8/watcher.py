import os
import time
import threading
import shutil
import yaml
from importlib import import_module

WATCH_DIR = "watch_dir"
UNPROCESSED = os.path.join(WATCH_DIR, "unprocessed")
UNDERPROCESS = os.path.join(WATCH_DIR, "underprocess")
PROCESSED = os.path.join(WATCH_DIR, "processed")

POLL_INTERVAL = 2  # seconds


def ensure_dirs():
    os.makedirs(UNPROCESSED, exist_ok=True)
    os.makedirs(UNDERPROCESS, exist_ok=True)
    os.makedirs(PROCESSED, exist_ok=True)


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


def process_file(file_path, monitor, trace_flag):
    filename = os.path.basename(file_path)
    temp_path = os.path.join(UNDERPROCESS, filename)
    # print(filename)
    try:

        shutil.move(file_path, temp_path)
        print("shutil done")

        run_pipeline("watch_dir/underprocess/test.txt", monitor=monitor,
                     trace_flag=trace_flag)
        print("run_pipeline done")

        shutil.move(temp_path, os.path.join(PROCESSED, filename))

    except Exception as e:
        monitor.log_error("pipeline", str(e))
        print(f"❌ Error processing {filename}: {e}")


def watch_folder(monitor, trace_flag=False):
    ensure_dirs()
    print(f"👀 Watching folder: {UNPROCESSED}")

    while True:
        print("🔁 Polling loop running...")
        try:
            files = [
                f for f in os.listdir(UNPROCESSED)
                if os.path.isfile(os.path.join(UNPROCESSED, f)) and f.endswith(".txt")
            ]

            for filename in files:
                file_path = os.path.join(UNPROCESSED, filename)
                process_file(file_path, monitor, trace_flag)

        except Exception as e:
            print(f"⚠️ Watcher error: {e}")

        time.sleep(POLL_INTERVAL)


def start_watcher(monitor, trace_flag=False):
    thread = threading.Thread(target=watch_folder, args=(
        monitor, trace_flag), daemon=True)
    thread.start()
    print("🌀 Watcher thread started.")
