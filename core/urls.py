from core.views import SubmitPhotoView, home, register
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

urlpatterns = [
    path("home", home, name="home"),
    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("register", register, name="register"),
    path("submit-photo", SubmitPhotoView.as_view(), name="submit-photo"),
    path(
        "logout",
        LogoutView.as_view(next_page=reverse_lazy("login")),
        name="logout",
    ),
]
