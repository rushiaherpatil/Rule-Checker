import logging
import os

# Create the logs directory if it doesn't exist
LOGS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
os.makedirs(LOGS_DIR, exist_ok=True)

# Configure a single logger for the application
LOG_FILE = os.path.join(LOGS_DIR, 'application.log')

logging.basicConfig(
    filename=LOG_FILE,  # Save logs in the logs/application.log file
    level=logging.INFO,  # Log INFO level and above
    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s'  # Include filename in the logs
)

logger = logging.getLogger(__name__)
