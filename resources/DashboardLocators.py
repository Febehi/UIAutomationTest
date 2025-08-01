from selenium.webdriver.common.by import By

class DashboardLocators:

    DASHBOARD_TITLE = (By.XPATH, "//h2[text()='Dashboard']")
    ADD_PRODUCT_BUTTON = (By.XPATH, "//button[.//span[text()='Add Product']]")
    ADD_FORM = (By.XPATH, "//div[@role='dialog' and .//h2[text()='Add Product']]")
    PRODUCT_NAME = (By.NAME, "name")
    DESCRIPTION = (By.NAME, "desc")
    PRICE = (By.NAME, "price")
    DISCOUNT = (By.NAME, "discount")
    DELETE_BUTTON=( By.XPATH, "//span[text()='Delete']" )
    SUCCESS_ALERT=(By.CSS_SELECTOR, "div.swal-modal[role='dialog'][aria-modal='true']")
    PRODUCTS_LIST=(By.CSS_SELECTOR, "table.MuiTable-root")
    OK_BUTTON = (By.XPATH, "//button[contains(@class, 'swal-button--confirm') and text()='OK']")
    EDIT_BUTTON = (By.XPATH, "//span[contains(@class, 'MuiButton-label') and text()='Edit']")
    EDIT_FORM=(By.XPATH, "//h2[text()='Edit Product']")
    EDIT_SUBMIT_BUTTON=(By.XPATH, "//span[text()='Edit Product']")
    CANCEL_BUTTON = (By.XPATH, "//button[.//span[text()='Cancel']]")










