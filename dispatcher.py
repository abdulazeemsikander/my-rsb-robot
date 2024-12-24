import csv
import logging
from queue import Queue

def fetch_data(input_file):
    queue = Queue()
    try:
        with open(input_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                queue.put(row)
        logging.info("Data successfully fetched and added to the queue.")
    except Exception as e:
        logging.error(f"Error reading input data: {e}")
    return queue
