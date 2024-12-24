from utils import setup_logger, get_credentials
from dispatcher import fetch_data
from performer import process_item
from state_machine import StateMachine
import logging

def main():
    setup_logger()
    logging.info("Starting Robot Execution")
    state_machine = StateMachine()

    try:
        # Initialization
        state_machine.transition_to("INITIALIZATION")
        username, password = get_credentials()
        input_file = "input_data.csv"
        transactions = fetch_data(input_file)

        if transactions.empty():
            raise ValueError("No transactions to process")

        # Processing
        state_machine.transition_to("PROCESSING")
        while not transactions.empty():
            item = transactions.get()
            try:
                process_item(item, username, password)
            except Exception as e:
                logging.error(f"Error processing item {item['ID']}: {e}")

        # Completion
        state_machine.transition_to("COMPLETION")
        logging.info("All transactions processed successfully.")

    except Exception as e:
        state_machine.transition_to("ERROR")
        logging.error(f"Bot encountered an error: {e}")
        raise

if __name__ == "__main__":
    main()
