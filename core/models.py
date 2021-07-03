from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
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
