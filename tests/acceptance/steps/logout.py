from time import sleep

from behave import when
from django.urls import reverse


@when("the user access logout page")
def logout(context):
    sleep(1)
    logout_button = context.driver.find_element_by_id("logout")
    logout_button.click()
