import logging
import sys

def get_logger():
    logger = logging.getLogger(name='twitter-bot')
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        logger.addHandler(handler)
    return logger