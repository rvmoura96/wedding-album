"""Hooks file."""
from behave.tag_matcher import ActiveTagMatcher
from django.contrib.auth import get_user_model
from faker import Faker
from ipdb import post_mortem
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from core.models import Photo


active_tag_value_provider = {"config_0": False}

active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)


def before_all(context):
    userdata = context.config.userdata
    context.config_0 = userdata.get("config_0", "False")
    browser = userdata.get("browser").lower()

    if browser == "chrome":
        context.driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install()
        )
    else:
        context.driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install()
        )


    context.server_url = userdata.get("server_url", "http://localhost:8000")


def before_feature(context, feature):
    ...


def before_scenario(context, scenario):
    context.faker = Faker()


def before_tag(context, tag):
    pass


def after_step(context, step):
    if context.config.userdata.get("debug") and step.status == "failed":
        post_mortem(step.exc_traceback)


def after_tag(context, tag):
    ...


def after_scenario(context, scenario):
    user_manager = get_user_model()
    user_manager.objects.all().delete()
    Photo.objects.all().delete()


def after_feature(context, feature):
    ...


def after_all(context):
    ...
    context.driver.quit()
