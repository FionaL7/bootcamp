# 1. Setup Logger
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.info("Logger initialized!")

# 2. Use Logging Levels
logger.debug("Debugging info")
logger.info("Just FYI")
logger.warning("This is a warning!")
logger.error("Something went wrong")

# 3. Contextual Messages
user = type("User", (), {"name": "Fiona"})()
logger.debug(f"User: {user.name}")

# 4. Suppress Print Statements
logger.info("Processing started")

# 5. Format Output

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# 6. File Logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger.info("This will go to app.log")

# 7. Use __name__ as Logger Name
logger = logging.getLogger(__name__)

# 8. Conditional Logging
debug = True
if debug:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

logger.debug("Only visible if debug=True")
