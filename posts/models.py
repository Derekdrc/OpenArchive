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
    abstract = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True)
    subject = models.CharField(max_length=8, choices=SUBJECT_CHOICES, default='Computer Science')
    date = models.DateTimeField(auto_now_add=True)
    #banner = models.ImageField(default='fallback.png', blank=True)
    pdf_file = models.FileField()
    license = models.CharField(max_length=8, choices=LICENSE_CHOICES, default='CC BY')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title