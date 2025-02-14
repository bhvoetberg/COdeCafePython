import logging.config

# Create a logging configuration
logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logging_examples2.log',
            'formatter': 'simple',
            'mode': 'a',  # append mode to file, create if not exists
        },
    },
    'loggers': {
        '': {
            'level': 'WARNING',
            'handlers': ['console', 'file'],
        },
    },
})

# Get the logger
logger = logging.getLogger('"Name of the application"')

logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.debug('This is a debug message')
print(logger, 'This is an info message')
