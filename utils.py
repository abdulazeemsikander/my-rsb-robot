import logging
from dotenv import load_dotenv
import os

def setup_logger():
    logging.basicConfig(
        filename='logs/robot.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Logger initialized.")

def get_credentials():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    if not username or not password:
        raise ValueError("Credentials are not set in the environment variables.")
    return username, password
