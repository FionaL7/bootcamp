import time
import logging
import psutil
import os
from functools import wraps

# Set up logging with context (user ID, function name)
logging.basicConfig(level=logging.DEBUG)

# Function to log with user context and function name


def log_with_context(user_id, func_name, message):
    logging.info(
        f"User ID: {user_id}, Function: {func_name}, Message: {message}")

# Function to track performance by adding timing to logs


def track_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(
            f"Function {func.__name__} executed in {end_time - start_time} seconds")
        return result
    return wrapper

# Function to add error IDs to log messages


def log_with_error_id(error_code, message):
    logging.error(f"Error Code: {error_code}, Message: {message}")


# Use an environment flag to enable verbose mode
DEBUG = True  # This can be set dynamically via environment variable
if DEBUG:
    logging.basicConfig(level=logging.DEBUG)

# Simple health check function


def health_check():
    return "System is running smoothly"


# Expose system performance metrics
metrics = {
    "function_calls": 0,
    "slow_functions": 0,
}

# Print current memory and CPU usage


def print_resource_usage():
    memory_info = psutil.virtual_memory()
    cpu_load = psutil.getloadavg()
    logging.info(f"Memory Usage: {memory_info.percent}%")
    logging.info(f"CPU Load: {cpu_load}")

# Decorator to trace function calls


def trace_function_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(
            f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

# Example usage:


# Health check
log_with_context(user_id=123, func_name="health_check", message=health_check())

# Function with performance tracking


@track_performance
def slow_function():
    time.sleep(2)
    return "Done"


slow_function()

# Log with error ID
log_with_error_id(404, "Resource not found")

# Print resource usage
print_resource_usage()

# Trace function calls


@trace_function_calls
def sample_function(x, y):
    return x + y


sample_function(5, 10)
