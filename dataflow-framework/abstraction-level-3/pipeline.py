import yaml
import importlib
from typing import List
from types import ModuleType
from type import ProcessorFunction


def import_by_path(path: str) -> ProcessorFunction:
    module_path, func_name = path.rsplit(".", 1)
    module: ModuleType = importlib.import_module(module_path)
    return getattr(module, func_name)


def get_yaml_pipeline(config_path: str) -> List[ProcessorFunction]:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    processors = []
    for step in config.get("pipeline", []):
        import_path = step["type"]
        fn = import_by_path(import_path)
        processors.append(fn)

    return processors
