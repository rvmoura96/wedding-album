from core.views import (
    CreateCommentaryView,
    PhotoApprovementListView,
    PhotoDetail,
    SubmitPhotoView,
    TimelineView,
    approve_photo,
    like_photo,
    register,
    repprove_photo,
)
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

urlpatterns = [
    path("", TimelineView.as_view(), name="home"),
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
    path("like-photo/<uuid:photo_uuid>", like_photo, name="photo-like"),
    path("photo/<int:pk>", PhotoDetail.as_view(), name="photo-detail"),
    path(
        "comment-photo", CreateCommentaryView.as_view(), name="photo-comment"
    ),
]
