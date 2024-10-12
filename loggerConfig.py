# logger_config.py

import logging
from logging.handlers import RotatingFileHandler

log_file_path = 'allLogs.log'

# Log rotation with a maximum file size of 1 MB and retaining up to 5 backup log files
handler = RotatingFileHandler(log_file_path, maxBytes=1000000, backupCount=5)

# Configure the logger with a custom format and the rotating file handler
logging.basicConfig(level=logging.INFO, handlers=[
                    handler], format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")