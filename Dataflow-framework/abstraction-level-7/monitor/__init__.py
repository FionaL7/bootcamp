
from collections import defaultdict, deque
from threading import Lock
import time
from config import MAX_TRACES, MAX_ERRORS


class Monitor:
    def __init__(self):
        self.metrics = defaultdict(
            lambda: {'count': 0, 'time': 0.0, 'errors': 0})
        self.traces = deque(maxlen=MAX_TRACES)
        self.errors = deque(maxlen=MAX_ERRORS)
        self.lock = Lock()

    def log_line(self, processor_name: str, elapsed: float, trace: list = None):
        with self.lock:
            self.metrics[processor_name]['count'] += 1
            self.metrics[processor_name]['time'] += elapsed
            if trace:
                self.traces.append(trace)

    def log_error(self, processor_name: str, message: str):
        with self.lock:
            self.metrics[processor_name]['errors'] += 1
            self.errors.append({
                'processor': processor_name,
                'message': message,
                'timestamp': time.time()
            })

    def get_stats(self):
        with self.lock:
            return dict(self.metrics)

    def get_traces(self):
        with self.lock:
            return list(self.traces)

    def get_errors(self):
        with self.lock:
            return list(self.errors)
