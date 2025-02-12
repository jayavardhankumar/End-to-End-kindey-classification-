import os
import sys
import logging

# Correct the logging format string: replace `%(messages)s` with `%(message)s`
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the logs directory and log file path
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure logging with both file and console handlers
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create the logger object
logger = logging.getLogger("kidneyClassifierLogger")
