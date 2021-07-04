from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.core.validators import FileExtensionValidator
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

    def create_user(self, email, password, **extra_fields):
        extra_fields["admin"] = False
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields["admin"] = True
        return self._create_user(email, password, **extra_fields)


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
    uploaded_by = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
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
