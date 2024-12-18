#Derek D'Arcy
from django import forms
from . import models
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'authors', 'affiliation', 'keywords', 'abstract', 'subject', 'pdf_file', 'license']


