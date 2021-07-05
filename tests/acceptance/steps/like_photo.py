from behave import then, when
from core.models import Photo
from expects import equal, expect


@when('the user click on "{button}"')
def step_impl(context, button):
    button = context.driver.find_element_by_id("like")
    button.click()


@then('the photo total likes should be "{likes_amount:d}"')
def step_impl(context, likes_amount):
    expected = likes_amount
    result = Photo.objects.filter(
        approved=True, likes__gte=likes_amount
    ).count()
    expect(expected).to(equal(result))
