from typing import Dict, Tuple, Iterator
import networkx as nx


class RoutingEngine:
    def __init__(self, routing_graph: Dict[str, str], processors: Dict[str, object]):
        self.graph = nx.DiGraph()
        self.routing_graph = routing_graph
        self.processors = processors

        for src, dest in routing_graph.items():
            self.graph.add_edge(src, dest)

    def run(self, input_lines: Iterator[str]) -> Iterator[str]:
        queue = [("start", line) for line in input_lines]

        while queue:
            tag, line = queue.pop(0)
            if tag == "end":
                yield line
                continue

            processor = self.processors.get(tag)
            if not processor:
                raise ValueError(f"No processor found for tag: {tag}")

            for next_tag, output_line in processor.process(iter([line])):
                queue.append((next_tag, output_line))
