from selenium.webdriver.common.by import By

class RegisterLocators:
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "confirm_password")
    SUCCESS_ALERT = (By.CLASS_NAME, "swal-modal")
    OK_BUTTON = (By.XPATH, "//button[contains(@class, 'swal-button--confirm') and text()='OK']")
    ERROR_ALERT= (By.CLASS_NAME, "swal-modal")


