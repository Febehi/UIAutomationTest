from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.register_locators import RegisterLocators
import yaml
import logging
import os

log_path = os.path.join('logs', 'app.log')
logging.basicConfig(filename=log_path, level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s : %(message)s')

# Add a separate handler for ERROR level messages
error_handler = logging.FileHandler(log_path)
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
error_handler.setFormatter(error_formatter)

# Attach the error handler to the root logger
logging.getLogger().addHandler(error_handler)
class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger()

    def is_displayed(self):
        return "register" in self.driver.current_url.lower()

    def enter_username(self, username):
        try:
            field = self.driver.find_element(*RegisterLocators.USERNAME)
            field.clear()
            field.send_keys(username)
            self.logger.info(f"Entered username: {username}")
        except Exception as e:
            self.logger.error(f"Failed to enter username: {e}")

    def enter_password(self, password):
        try:
            field = self.driver.find_element(*RegisterLocators.PASSWORD)
            field.clear()
            field.send_keys(password)
            self.logger.info(f"Entered password")
        except Exception as e:
            self.logger.error(f"Failed to enter password: {e}")

    def enter_confirm_password(self, confirm_password):
        try:
            field = self.driver.find_element(*RegisterLocators.CONFIRM_PASSWORD)
            field.clear()
            field.send_keys(confirm_password)
            self.logger.info(f"Entered confirm password")
        except Exception as e:
            self.logger.error(f"Failed to enter confirm password: {e}")

    def click_register_button(self):
        try:
            self.driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()
            self.logger.info("Clicked Register button")
        except Exception as e:
            self.logger.error(f"Failed to click Register button: {e}")

    def get_success_alert(self):
        try:
            alert_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(RegisterLocators.SUCCESS_ALERT)
            ).text
            self.logger.info(f"Success alert received: {alert_text}")
            return alert_text
        except Exception as e:
            self.logger.error(f"Failed to get success alert: {e}")
            return ""

    def click_ok_button(self):
        try:
            ok_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(RegisterLocators.OK_BUTTON)
            )
            ok_button.click()
            self.logger.info("Clicked OK button in alert")
        except Exception as e:
            self.logger.error(f"Failed to click OK button: {e}")


    def get_error_alert(self):
        try:
            alert_text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(RegisterLocators.ERROR_ALERT)
            ).text
            self.logger.info(f"Error alert received: {alert_text}")
            return alert_text
        except Exception as e:
            self.logger.error(f"Failed to get error alert: {e}")
            return ""

