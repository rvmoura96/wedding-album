from core.views import SubmitPhotoView, home, register
from django.contrib.auth.views import LoginView
from django.urls import path

urlpatterns = [
    path("home", home, name="home"),
    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("register", register, name="register"),
    path("submit-photo", SubmitPhotoView.as_view(), name="submit-photo"),
]
