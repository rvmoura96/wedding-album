from behave import given, then, when
from django.contrib.auth import get_user_model
from faker import Faker
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from wedding-album.core.models import CustomUser
from modules.auxiliar import cast_table_to_dict


@given(u'a guest data')
def step_impl(context):
    context.guest = cast_table_to_dict(context.table)


@when(u'the guests form is filled with guest data')
def step_impl(context):
    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install()
    )
    faker = Faker()
    user_password = faker.password()

    #TODO: MOVE TO A PAGE OBJECT
    driver.get("http://localhost:8000/wedding/register")


    name = driver.find_element_by_id('id_first_name')
    name.send_keys(context.guest['name'])

    last_name = driver.find_element_by_id('id_last_name')
    last_name.send_keys(context.guest['last_name'])

    email = driver.find_element_by_id('id_email')
    email.send_keys(context.guest['email'])

    password1 = driver.find_element_by_id('id_password1')
    password1.send_keys(user_password)

    password2 = driver.find_element_by_id('id_password2')
    password2.send_keys(user_password)

    submit = driver.find_element_by_tag_name('button')
    submit.click()


@then(u'the user should be registered')
def step_impl(context):
    import ipdb; ipdb.sset_trace()
    result = CustomUser.objects.filter(email=context.guest['email']).count()

    raise NotImplementedError(u'STEP: Then the user should be registered')
