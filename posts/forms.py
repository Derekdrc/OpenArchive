from django import forms
from . import models
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'pdf_file']


