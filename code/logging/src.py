import logging
import logging.config

# Load the logging configuration from the file
logging.config.fileConfig('logging.conf')

# Create a logger for the example
logger = logging.getLogger('simpleExample')

# Log some messages
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
