from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.core.validators import FileExtensionValidator
from django.db import models


class UserManager(BaseUserManager):
    ...


class CustomUser(AbstractBaseUser):
    objects = UserManager()
    username = None
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    required_field = []


class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid4)
    file = models.FileField(
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "jpg",
                    "jpeg",
                    "png",
                ]
            )
        ]
    )
    approved = models.BooleanField(default=False)
