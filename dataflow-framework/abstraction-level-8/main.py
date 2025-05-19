import argparse
import time
from monitor.metrics import Monitor
from dashboard.api import start_dashboard
from watcher import start_watcher  # this is new


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--trace', action='store_true',
                        help='Enable trace tracking')
    parser.add_argument('--port', type=int, default=8000,
                        help='Port for dashboard')
    args = parser.parse_args()

    # 🧠 Initialize monitor
    monitor = Monitor(trace_enabled=args.trace)

    # 🌐 Start dashboard
    start_dashboard(monitor, port=args.port)

    # 👀 Start file watcher
    start_watcher(monitor, trace_flag=args.trace)

    # 🧘‍♀️ Keep program alive (simulate long-running service)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("👋 Exiting gracefully...")


if __name__ == '__main__':
    main()
