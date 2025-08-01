from behave import given, when, then
from pages.register_page import RegisterPage
import logging
import allure

def save_screenshot(context, name):
    context.driver.save_screenshot(name)
    allure.attach(context.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)


@given("I am on the register page")
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    assert context.register_page.is_displayed()
    save_screenshot(context, "register_page.png")


@when('I enter my username "{username}"')
def step_impl(context, username):
    context.register_page.enter_username(username)
    save_screenshot(context, "entered_username.png")


@when('I enter my password "{password}"')
def step_impl(context, password):
    context.register_page.enter_password(password)
    save_screenshot(context, "entered_password.png")


@when('I enter my confirm password "{confirm_password}"')
def step_impl(context, confirm_password):
    context.register_page.enter_confirm_password(confirm_password)
    save_screenshot(context, "entered_confirm_password.png")


@when("I click on the Register button")
def step_impl(context):
    context.register_page.click_register_button()
    logging.info("Clicked on Register button")
    save_screenshot(context, "register_button_clicked.png")


@then('I should receive a success alert "{alert}"')
def step_impl(context, alert):
    actual_alert = context.register_page.get_success_alert()
    assert actual_alert == alert, f"Expected: '{alert}', Got: '{actual_alert}'"
    logging.info("Success alert is shown")
    save_screenshot(context, "success_alert.png")


@then('I should receive an error alert "{alert}"')
def step_impl(context, alert):
    actual_alert = context.register_page.get_error_alert()
    assert actual_alert == alert, f"Expected: '{alert}', Got: '{actual_alert}'"
    logging.info("Error alert is shown")
    save_screenshot(context, "error_alert.png")



@then("Click on the OK button")
def step_impl(context):
    context.register_page.click_ok_button()
    logging.info("Clicked OK on alert")
    save_screenshot(context, "clicked_ok_alert.png")


@then("I will be redirect to the login page")
def step_impl(context):
    from pages.login_page import LoginPage
    context.login_page = LoginPage(context.driver)
    assert context.login_page.is_displayed()
    logging.info("Successfully redirected to login page")
    save_screenshot(context, "redirected_to_login.png")
