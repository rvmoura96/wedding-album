from behave import given, then, when
from core.models import CustomUser
from django.contrib.auth import get_user_model
from expects import equal, expect
from faker import Faker
from modules.auxiliar import cast_table_to_dict


@given(u"a guest data")
def step_impl(context):
    context.guest = cast_table_to_dict(context.table)


@when(u"the guest form is filled with guest data")
def step_impl(context):
    faker = Faker()
    user_password = faker.password()

    # TODO: MOVE TO A PAGE OBJECT
    context.driver.get("http://localhost:8000/wedding/register")

    name = context.driver.find_element_by_id("id_first_name")
    name.send_keys(context.guest["name"])

    last_name = context.driver.find_element_by_id("id_last_name")
    last_name.send_keys(context.guest["last_name"])

    email = context.driver.find_element_by_id("id_email")
    email.send_keys(context.guest["email"])

    password1 = context.driver.find_element_by_id("id_password1")
    password1.send_keys(user_password)

    password2 = context.driver.find_element_by_id("id_password2")
    password2.send_keys(user_password)

    submit = context.driver.find_element_by_tag_name("button")
    submit.click()


@then(u"the guest should be registered")
def step_impl(context):
    user_manager = get_user_model()

    result = user_manager.objects.filter(email=context.guest["email"]).exists()
    expected = True
    expect(expected).to(equal(result))


@then(u'the number of registred users should be "{total_users:d}"')
def step_impl(context, total_users):
    user_manager = get_user_model()
    result = user_manager.objects.count()
    expected = total_users
    expect(expected).to(equal(result))