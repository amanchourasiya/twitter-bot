import logging
import sys

def get_logger():
    logger = logging.getLogger(name='twitter-bot')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger