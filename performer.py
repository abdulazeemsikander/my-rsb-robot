import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def process_item(item, username, password, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            driver = webdriver.Chrome()
            driver.get("https://robotsparebinindustries.com/")

            # Login
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login").click()

            # Process Transaction
            driver.find_element(By.ID, "item_input").send_keys(item['ID'])
            driver.find_element(By.ID, "submit").click()
            time.sleep(2)

            logging.info(f"Successfully processed item {item['ID']}")
            driver.quit()
            return  # Exit on success
        except Exception as e:
            attempt += 1
            logging.error(f"Attempt {attempt} failed for item {item['ID']}: {e}")
            if attempt == retries:
                logging.error(f"Item {item['ID']} failed after {retries} attempts.")
                break
            time.sleep(5)  # Wait before retrying
