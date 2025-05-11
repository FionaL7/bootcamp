from fastapi import FastAPI
import threading
import uvicorn

app = FastAPI()
monitor = None


@app.get("/stats")
def stats():

    return monitor.get_stats()


@app.get("/trace")
def trace():
    return monitor.get_traces()


@app.get("/errors")
def errors():
    return monitor.get_errors()


def start_dashboard(monitor_instance, port=8000):
    global monitor
    monitor = monitor_instance

    def run():
        uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")

    print(f"🌐 Dashboard running at http://localhost:{port}")
    thread = threading.Thread(target=run)
    thread.start()
