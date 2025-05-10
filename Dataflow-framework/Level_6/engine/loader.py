import yaml
import importlib


def load_config(path: str):
    with open(path) as f:
        return yaml.safe_load(f)


def build_pipeline(config: dict):
    processors = {}
    for tag, path in config["processors"].items():
        if path == "end":
            continue
        module_path, class_name = path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        processors[tag] = cls()
    return processors
