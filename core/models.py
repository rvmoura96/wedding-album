from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUser(AbstractBaseUser):
    username = None
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    required_field = []


class UserManager(BaseUserManager):
    ...
