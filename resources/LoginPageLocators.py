from selenium.webdriver.common.by import By

class LoginPageLocators:

    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//span[contains(@class, 'MuiButton-label')]")
    OK_BUTTON = (By.CSS_SELECTOR, "button.swal-button.swal-button--confirm")

