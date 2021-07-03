from core.views import home, register
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path("register", register, name="register"),
    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("home", home, name="home"),
]
