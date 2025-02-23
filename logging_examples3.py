# >= 3.12 due to queue_handler listener
import atexit
import logging.config
import logging.handlers
import json

logger = logging.getLogger('"Name of the application"')

with open('logging_examples3_config.json') as file:
    try:
        config = json.load(file)
        logging.config.dictConfig(config)
        queue_handler = logging.getHandlerByName("queue_handler")
        if queue_handler is not None:
            queue_handler.listener.start()
            atexit.register(queue_handler.listener.stop)
        print("Logging configuration of",logger.name, "loaded successfully")
    except FileNotFoundError:
        logging.basicConfig(level=logging.INFO)
        logging.warning("Config file not found, using basic configuration - level = INFO")
    except json.JSONDecodeError:
        logging.basicConfig(level=logging.INFO)
        logging.error("Invalid JSON in config file")


logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.debug('This is a debug message')