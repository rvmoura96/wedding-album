from core.views import (
    PhotoApprovementListView,
    SubmitPhotoView,
    approve_photo,
    register,
    repprove_photo,
    TimelineView
)
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

urlpatterns = [
    path("home", TimelineView.as_view(), name="home"),
    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("register", register, name="register"),
    path("submit-photo", SubmitPhotoView.as_view(), name="submit-photo"),
    path(
        "logout",
        LogoutView.as_view(next_page=reverse_lazy("login")),
        name="logout",
    ),
    path(
        "photo-approvement",
        PhotoApprovementListView.as_view(),
        name="photo-approvement",
    ),
    path(
        "photo-approve/<uuid:photo_uuid>", approve_photo, name="photo-approve"
    ),
    path(
        "photo-repprove/<uuid:photo_uuid>",
        repprove_photo,
        name="photo-repprove",
    ),
]
