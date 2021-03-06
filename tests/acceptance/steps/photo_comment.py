from time import sleep

from behave import then, when
from expects import equal, expect

from core.models import Photo


@when("a user acess a photo page")
def step_impl(context):
    sleep(1)
    photo = context.driver.find_element_by_id("photo-detail")
    photo.click()


@when(u'comment "{comment_content}"')
def step_impl(context, comment_content):
    sleep(1)
    comment_area = context.driver.find_element_by_id("id_content")
    comment_area.send_keys(comment_content)
    submit_button = context.driver.find_element_by_id("id_comment")
    submit_button.click()


@then(u'the photo should have "{comments_amount}" commentary')
def step_impl(context, comments_amount):
    result = Photo.objects.filter(
        approved=True, commentary__gte=comments_amount
    ).count()
    expected = 1
    expect(expected).to(equal(result))
