from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
