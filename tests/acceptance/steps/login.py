from behave import given, then, when
from django.urls import reverse
from expects import equal, expect
from time import sleep


@given("a user accessing the login page")
def access_login_page(context):
    context.driver.get(f"{reverse('login')}")


@when('the user fill the login form with "{credentials_status}" credentials')
def fill_login_form(context, credentials_status):
    PASSWORDS = {
        "correct": context.guest["password"],
        "incorrect": "incorrect password",
    }
    sleep(1)
    email = context.driver.find_element_by_id("id_username")
    email.send_keys(context.guest["email"])
    password = context.driver.find_element_by_id("id_password")
    password.send_keys(PASSWORDS[credentials_status])
    submit = context.driver.find_element_by_id("login")
    submit.click()


@then('the user should be redirected to "{page_name}"')
def assert_login_redirect(context, page_name):
    result = context.driver.current_url.split("8000")[-1]
    expected = reverse(page_name)
    expect(expected).to(equal(result))
