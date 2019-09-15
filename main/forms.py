from django import forms

from .models import Comment
from .models import Notice


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', ]


class NoticeForm(forms.ModelForm):
    
    class Meta:
        model = Notice
        fields = ['name', 'text', ]
