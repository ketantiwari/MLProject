import logging
import os
from datetime import datetime
import sys

from src.exception import customeexception

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.path.dirname(__file__), 'app.log')
os.makedirs(logs_path, exist_ok=True)


Log_file_path = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=Log_file_path,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

