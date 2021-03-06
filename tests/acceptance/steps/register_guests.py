from time import sleep

from behave import given, then, when
from django.contrib.auth import get_user_model
from django.urls import reverse
from expects import equal, expect

from modules.auxiliar import cast_table_to_dict


@given("a guest data")
def step_impl(context):
    context.guest = cast_table_to_dict(context.table)


@when("the user access the platform")
def step_impl(context):
    context.driver.get(context.server_url)


@when("click on sign up")
def step_impl(context):
    sleep(1)
    sign_up = context.driver.find_element_by_id("sign_up")
    sign_up.click()


@when("the guest form is filled with guest data")
def step_impl(context):
    context.guest["password"] = context.faker.password()

    # TODO: MOVE TO A PAGE OBJECT
    context.driver.get(f"{context.server_url}{reverse('register')}")
    sleep(1)

    name = context.driver.find_element_by_id("id_first_name")
    name.send_keys(context.guest["first_name"])

    last_name = context.driver.find_element_by_id("id_last_name")
    last_name.send_keys(context.guest["last_name"])

    email = context.driver.find_element_by_id("id_email")
    email.send_keys(context.guest["email"])

    password1 = context.driver.find_element_by_id("id_password1")
    password1.send_keys(context.guest["password"])

    password2 = context.driver.find_element_by_id("id_password2")
    password2.send_keys(context.guest["password"])

    submit = context.driver.find_element_by_id("sign_up")
    submit.click()
    sleep(1)


@then("the guest should be registered")
def step_impl(context):
    user_manager = get_user_model()

    result = user_manager.objects.filter(email=context.guest["email"]).exists()
    expected = True
    expect(expected).to(equal(result))


@then('the number of registred users should be "{total_users:d}"')
def step_impl(context, total_users):
    user_manager = get_user_model()
    result = user_manager.objects.count()
    expected = total_users
    expect(expected).to(equal(result))
