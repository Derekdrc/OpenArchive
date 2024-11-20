from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


SUBJECT_CHOICES = (
    ('CS', 'Computer Science'),
    ('Eng', 'Engineering'),
    ('Engl', 'English'),
    ('Arch', 'Architecture'),
    ('Bus', 'Business'),
    ('Com', 'Communications'),
)

LICENSE_CHOICES = (
    ('BY', 'CC BY'),
    ('SA', 'CC BY-SA'),
    ('NC', 'CC BY-NC'),
    ('BYNCSA', 'CC BY-NC-SA'),
    ('ND', 'CC BY-NC-ND'),
)
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255, default=" ", help_text="Please use full names separated by commas")
    affiliation = models.CharField(max_length=255, default="LTU")
    keywords = models.CharField(max_length=255, default="Thesis", help_text="Please separate keywords by commas")
    abstract = models.TextField(help_text="Copy and Paste your abstract or introduction into this field")
    slug = AutoSlugField(populate_from='title', unique=True)
    subject = models.CharField(max_length=8, choices=SUBJECT_CHOICES, default='Computer Science')
    date = models.DateTimeField(auto_now_add=True)
    #banner = models.ImageField(default='fallback.png', blank=True)
    pdf_file = models.FileField()
    license = models.CharField(max_length=8, choices=LICENSE_CHOICES, default='CC BY')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title