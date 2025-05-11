import yaml
import importlib
from typing import Iterator


def load_pipeline(config_file: str):
    with open(config_file) as f:
        config = yaml.safe_load(f)

    processors = []
    for step in config["pipeline"]:
        type_path = step["type"]
        options = step.get("config", {})

        module_path, class_name = type_path.rsplit(".", 1)
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)

        processor = cls(**options) if options else cls()
        processors.append(processor)
    return processors


def run_pipeline(processors, stream: Iterator[str]) -> Iterator[str]:
    for processor in processors:
        stream = processor.process(stream)
    return stream
