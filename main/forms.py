from django import forms
from .models import *

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text', ]

# class AddPlacesForm(forms.ModelForm):
#     class Meta:
#         model = Place
#         fields = ['category', 'name', 'image', 'description', 'address',]
      