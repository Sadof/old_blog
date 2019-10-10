from django import forms
from .models import  Comment,Post
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm, Textarea, DateTimeInput


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        labels = {'text': _('Enter your Comment'), }

class addPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["post_title","post_text","pub_date"]
        widgets = {
            "post_text": Textarea(attrs={'cols': 80, 'rows': 20}),
            "pub_date" : DateTimeInput()
        }
