from loguru import logger
import sys

__version__ = "0.1.1"

logger.remove()
logger.add(sys.stdout, level="INFO")
