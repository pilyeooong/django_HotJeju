from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import *

User = get_user_model()

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class SignupForm(UserCreationForm):
    username = forms.CharField(label='아이디', widget=forms.TextInput(attrs={'pattern': '[a-zA-Z0-9]+', 'title': '특수문자, 공백 입력불가',}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('이미 사용중인 아이디입니다.')
        return username
    
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('비밀번호와 비밀번호 확인란의 값이 일치하지 않습니다')
        return password2

    def save(self):
        if self.is_valid():
            return User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password2']
            )

