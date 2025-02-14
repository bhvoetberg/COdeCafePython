import logging.config
import json

# Load the logging configuration from a JSON file
with open('logging_config.json') as file:
    config = json.load(file)

logging.config.dictConfig(config)

# Get the logger
logger = logging.getLogger('"Name of the application"')

logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.debug('This is a debug message')