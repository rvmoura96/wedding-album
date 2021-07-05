from behave import when
from django.urls import reverse


@when("the user access logout page")
def logout(context):
    context.driver.get(f"http://localhost:8000{reverse('logout')}")
