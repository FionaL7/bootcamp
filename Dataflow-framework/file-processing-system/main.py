import argparse
import time
from pipeline import run_pipeline
from watcher import start_watcher
from monitor import Monitor
from api import start_dashboard


def main():
    parser = argparse.ArgumentParser(description="Pipeline File Processor")
    parser.add_argument('--input', type=str,
                        help="Run in single-file mode with given file path")
    parser.add_argument('--watch', action='store_true',
                        help="Run in watch mode")
    parser.add_argument('--trace', action='store_true',
                        help="Enable trace logging")

    args = parser.parse_args()
    monitor = Monitor()

    # Start dashboard
    start_dashboard(monitor)

    if args.input:
        print(f"🚀 Running pipeline on: {args.input}")
        run_pipeline(args.input, monitor, trace_flag=args.trace)
    elif args.watch:
        print("👀 Watch mode enabled")
        start_watcher(monitor, trace_flag=args.trace)
        while True:
            print("🔁 Polling loop running...")
            time.sleep(5)
    else:
        print("⚠️ Please specify either --input or --watch")


if __name__ == "__main__":
    main()
