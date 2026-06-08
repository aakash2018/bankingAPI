import os
from loguru import logger
from .config import settings

logger.remove()  # Remove default logger


LOG_DIR =os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs")
LOG_FORMAT=("{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}")

logger.add(
    sink = os.path.join(LOG_DIR, "debug.log"),
    format=LOG_FORMAT, 
    rotation="10MB", 
    retention="7 days", 
    compression="zip", 
    level="DEBUG" if settings.ENVIRONMENT == "local" else "INFO",
    filter=lambda record: record["level"].no <= logger.level("WARNING").no,
    backtrace=True,
    diagnose=True
)

def get_logger(name: str):
    return logger.bind(name=name)