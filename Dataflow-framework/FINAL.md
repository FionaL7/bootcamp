# FINAL.md

## 1. **Design Decisions**

The foundation of the system was built incrementally, starting with a basic script that read from standard input and processed lines. As complexity grew, we adopted a modular architecture centered around processors and a routing engine. Each processor performed a specific transformation or validation, and the system routed lines based on tags.

Key architectural choices included:

- **Tag-based routing**: Using tags to guide the flow of data between processors offered a clean abstraction for conditional and multi-path logic.
- **Stateless processors**: Keeping processors stateless made the system more testable, composable, and safe for future parallelization.
- **Observability hooks**: Integrating observability in a non-intrusive way allowed us to monitor the system without altering business logic.
- **Threaded web dashboard**: Running the FastAPI server in a separate thread helped decouple visualization from core execution.

These design choices helped us maintain a balance between extensibility, simplicity, and operational transparency.

## 2. **Tradeoffs**

To keep the system manageable, several simplifications were made:

- We used **in-memory data structures** for metrics, traces, and errors instead of a database or persistent store.
- The **FastAPI dashboard** serves basic JSON rather than a full frontend UI, prioritizing function over form.
- Processors are **synchronous and single-threaded**, which simplifies development but limits scalability.
- **Retry logic** and fault handling are basic—robust fault tolerance mechanisms (e.g., exponential backoff or queue-based retries) were not implemented.

These choices allowed faster development and clarity of purpose, but they also mean the system has limitations in high-availability or high-throughput scenarios.

## 3. **Scalability**

The current system works well for modest workloads, but to handle significantly larger inputs or support multiple users, we would need:

- **Parallel processing**: Move from simple threading to multiprocessing or asynchronous execution.
- **External storage**: Use message queues (e.g., RabbitMQ, Kafka) for buffering and databases for persistence.
- **Optimized data handling**: Introduce line batching and streaming for large file inputs to reduce memory usage.
- **Distributed observability**: Offload metrics and tracing to tools like Prometheus, Grafana, or OpenTelemetry.

The architecture supports these changes conceptually but would need technical upgrades to scale in practice.

## 4. **Extensibility & Security**

To make this suitable for real-world deployment:

- We would secure the dashboard with **authentication and authorization**, especially if exposed over the network.
- File inputs would need **validation and size limits** to prevent abuse or crashes.
- We'd protect outputs by using **role-based access control** and possibly encrypting stored files.
- For long-running or multi-user environments, **resource limits, sandboxing, and audit logging** would be necessary.

The modularity of the system makes it easy to add new processors, enhance routing logic, or plug in third-party observability tools. With some production hardening, this could evolve into a robust data processing framework.
