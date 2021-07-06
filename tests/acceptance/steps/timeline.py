from time import sleep

from behave import then, when
from django.urls import reverse
from expects import equal, expect


@when("a user access the timeline")
def foo(context):
    context.driver.get(f"http://localhost:8000{reverse('home')}")


@then("the timeline should list all approved photos")
def bar(context):
    expected = True
    sleep(1)
    result = bool(context.driver.find_element_by_id("like"))
    expect(expected).to(equal(result))
