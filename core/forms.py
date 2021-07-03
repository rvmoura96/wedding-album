from django.contrib.auth import get_user_model

from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )
