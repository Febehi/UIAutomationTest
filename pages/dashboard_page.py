from resources.DashboardLocators import DashboardLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os

log_path = os.path.join('logs', 'app.log')
logging.basicConfig(filename=log_path, level=logging.INFO, filemode='a', format='%(asctime)s - %(levelname)s : %(message)s')

# Separate handler for ERROR level
error_handler = logging.FileHandler(log_path)
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
error_handler.setFormatter(error_formatter)
logging.getLogger().addHandler(error_handler)


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def is_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(DashboardLocators.DASHBOARD_TITLE))
            self.logger.info("Dashboard is displayed.")
            return True
        except Exception as e:
            self.logger.error(f"Dashboard is not displayed: {e}")
            return False

    def click_add_product_button(self):
        try:
            self.driver.find_element(*DashboardLocators.ADD_PRODUCT_BUTTON).click()
            self.logger.info("Clicked on Add Product button.")
        except Exception as e:
            self.logger.error(f"Failed to click Add Product button: {e}")

    def is_add_form_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(DashboardLocators.ADD_FORM))
            self.logger.info("Add Product Form is displayed.")
            return True
        except Exception as e:
            self.logger.error(f"Add Product Form not displayed: {e}")
            return False

    def enter_product_name(self, name):
        try:
            field = self.driver.find_element(*DashboardLocators.PRODUCT_NAME)
            field.clear()
            field.send_keys(name)
            self.logger.info(f"Entered product name: {name}")
        except Exception as e:
            self.logger.error(f"Failed to enter product name: {e}")

    def enter_description(self, description):
        try:
            field = self.driver.find_element(*DashboardLocators.DESCRIPTION)
            field.clear()
            field.send_keys(description)
            self.logger.info(f"Entered product description: {description}")
        except Exception as e:
            self.logger.error(f"Failed to enter description: {e}")

    def enter_price(self, price):
        try:
            field = self.driver.find_element(*DashboardLocators.PRICE)
            field.clear()
            field.send_keys(str(price))
            self.logger.info(f"Entered product price: {price}")
        except Exception as e:
            self.logger.error(f"Failed to enter price: {e}")

    def enter_discount(self, discount):
        try:
            field = self.driver.find_element(*DashboardLocators.DISCOUNT)
            field.clear()
            field.send_keys(str(discount))
            self.logger.info(f"Entered product discount: {discount}")
        except Exception as e:
            self.logger.error(f"Failed to enter discount: {e}")

    def click_add_product_submit(self):
        try:
            self.driver.find_element(*DashboardLocators.SUBMIT_BUTTON).click()
            self.logger.info("Clicked on Submit button for Add Product.")
        except Exception as e:
            self.logger.error(f"Failed to submit the Add Product form: {e}")

    def click_delete_button(self):
        try:
            delete_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DashboardLocators.DELETE_BUTTON)
            )
            delete_button.click()
            self.logger.info("Clicked the Delete button.")
        except Exception as e:
            self.logger.error(f"Failed to click the Delete button: {e}")

    def get_success_message(self, expected_text):
        try:
            alert_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(DashboardLocators.SUCCESS_ALERT)
            )
            alert_text = alert_element.text.strip()
            assert alert_text == expected_text, f"Expected alert text '{expected_text}', but got '{alert_text}'"
            self.logger.info(f"Success alert displayed: {alert_text}")
            return alert_text
        except Exception as e:
            self.logger.error(f"Failed to verify success alert: {e}")
            raise

    def is_product_deleted(self):
        try:
            products = self.driver.find_elements(*DashboardLocators.PRODUCTS_LIST)
            is_deleted = len(products) == 0
            self.logger.info(f"Product deletion status: {is_deleted}")
            return is_deleted
        except Exception as e:
            self.logger.error(f"Failed to check product deletion: {e}")
            return False

    def click_ok_button(self):
        try:
            ok_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DashboardLocators.OK_BUTTON)
            )
            ok_button.click()
            self.logger.info("Clicked the OK button.")
        except Exception as e:
            self.logger.error(f"Failed to click the OK button: {e}")

    def click_edit_button(self):
        try:
            edit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DashboardLocators.EDIT_BUTTON)
            )
            edit_button.click()
            self.logger.info("Clicked the Edit button.")
        except Exception as e:
            self.logger.error(f"Failed to click the Edit button: {e}")

    def is_edit_form_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(DashboardLocators.EDIT_FORM)
            )
            self.logger.info("Edit Product form is displayed.")
            return True
        except Exception as e:
            self.logger.error(f"Edit Product form not displayed: {e}")
            return False
        
    def click_edit_product_submit(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DashboardLocators.EDIT_SUBMIT_BUTTON)
            )
            submit_button.click()
            self.logger.info("Clicked the Submit button for Edit Product.")
        except Exception as e:
            self.logger.error(f"Failed to click the Submit button for Edit Product: {e}")

    def click_cancel_button(self):
        try:
            cancel_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(DashboardLocators.CANCEL_BUTTON)
            )
            cancel_button.click()
            self.logger.info("Clicked on the Cancel button.")
        except Exception as e:
            self.logger.error(f"Failed to click on the Cancel button: {e}")







    
