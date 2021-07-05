from behave import given, then, when
from django.urls import reverse

from core.models import Photo
from expects import equal, expect
from helpers.constants import ASSETS_DIR


@given("the user access the photo submission page")
def step_impl(context):
    context.driver.get(f"http://localhost:8000{reverse('submit-photo')}")


@when('the user try submmit a "{file_type}"')
def step_impl(context, file_type):
    FILES = {
        "pdf": f"{ASSETS_DIR}/pdf/sokka.pdf",
        "photo": f"{ASSETS_DIR}/img/sokka.jpg",
    }
    file = context.driver.find_element_by_id("id_file")
    file.send_keys(FILES[file_type])
    submit = context.driver.find_element_by_tag_name("button")
    submit.click()


@then('the number of photos to be approved should be "{expected:d}"')
def step_impl(context, expected):
    result = Photo.objects.filter(approved=False).count()
    expect(expected).to(equal(result))
