from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', ]

# class AddPlacesForm(forms.ModelForm):
#     class Meta:
#         model = Place
#         fields = ['category', 'name', 'image', 'description', 'address',]
