from django import forms

from .models import BlogsPost

class PostForm(forms.ModelForm):

    class Meta:
        model = BlogsPost
        fields = ('title', 'body',)