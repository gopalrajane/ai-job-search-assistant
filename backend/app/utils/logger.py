import logging
from pythonjsonlogger import jsonlogger
import sys
from app.config import settings

def setup_logging():
    """Setup structured JSON logging"""
    root_logger = logging.getLogger()
    root_logger.setLevel(settings.LOG_LEVEL)
    
    # Console handler with JSON formatter
    console_handler = logging.StreamHandler(sys.stdout)
    json_formatter = jsonlogger.JsonFormatter()
    console_handler.setFormatter(json_formatter)
    root_logger.addHandler(console_handler)
    
    # File handler
    file_handler = logging.FileHandler('logs/app.log')
    file_handler.setFormatter(json_formatter)
    root_logger.addHandler(file_handler)
    
    return root_logger

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
