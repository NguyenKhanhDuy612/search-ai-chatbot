import logging
import sys


def setup_logging(logger=logging.getLogger(), level=logging.INFO):
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    file_handler = logging.FileHandler('log.log')
    logger.addHandler(file_handler)
    logger.addHandler(handler)
    logger.setLevel(level)
