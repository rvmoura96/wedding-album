from behave import when


@when("the user access logout page")
def logout(context):
    context.driver.get("http://localhost:8000/wedding/logout")
