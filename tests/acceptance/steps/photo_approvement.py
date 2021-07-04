from behave import given, then, when
from core.models import Photo
from django.contrib.auth import get_user_model
from django.urls import reverse
from expects import equal, expect
from modules.auxiliar import cast_table_to_dict


@given("an engaged data")
def create_engaged_user(context):
    engaged_data = cast_table_to_dict(context.table)
    email = engaged_data["email"]
    del engaged_data["email"]

    password = context.faker.password()
    context.engaged = {"email": email, "password": password}

    user_manager = get_user_model()

    super_user = user_manager.objects.create_superuser(
        email, password, **engaged_data
    )


@when("an enageg login")
def step_impl(context):
    # TODO: MOVE TO PAGEOBJECTS

    context.driver.get(f"http://localhost:8000{reverse('login')}")
    email = context.driver.find_element_by_id("id_username")
    email.send_keys(context.engaged["email"])
    password = context.driver.find_element_by_id("id_password")
    password.send_keys(context.engaged["password"])
    submit = context.driver.find_element_by_tag_name("button")
    submit.click()


@when("an engaged access the photo approvement page")
def step_impl(context):
    context.driver.get(f"http://localhost:8000{reverse('photo-approvement')}")


@when('an engaged click on "{action}"')
def step_impl(context, action):
    approve_button = context.driver.find_element_by_id(action)
    approve_button.click()


@then('the approved photos number should be "{total_photos:d}"')
def step_impl(context, total_photos):
    expected = total_photos
    result = Photo.objects.filter(approved=True).count()
    expect(expected).to(equal(result))


@when("a guest try to access the photo approvement page")
def step_impl(context):
    context.driver.get(f"http://localhost:8000{reverse('photo-approvement')}")


@then("the guest should be redirected to home page")
def step_impl(context):
    result = context.driver.current_url.split("8000")[-1]
    expected = reverse("home")
    expect(expected).to(equal(result))


@then('the total of photos should be "{total_photos:d}"')
def assert_total_of_photos(context, total_photos):
    expected = total_photos
    result = Photo.objects.count()
    expect(expected).to(equal(result))
