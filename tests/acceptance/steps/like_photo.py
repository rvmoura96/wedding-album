from time import sleep

from behave import then, when
from expects import equal, expect

from core.models import Photo


@when('the user click on "{button}"')
def step_impl(context, button):
    sleep(1)
    button = context.driver.find_element_by_id("like")
    button.click()


@then('the photo total likes should be "{likes_amount:d}"')
def step_impl(context, likes_amount):
    expected = likes_amount
    sleep(1)
    likes = context.driver.find_element_by_id("total_likes")
    result = int(likes.text)
    expect(expected).to(equal(result))
