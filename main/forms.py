from django import forms
from .models import *

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text', ]

class AddForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ['category', 'name', 'image', 'description', 'address',]
