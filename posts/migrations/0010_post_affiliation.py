# Generated by Django 5.1.1 on 2024-11-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_post_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='affiliation',
            field=models.CharField(default='LTU', max_length=255),
        ),
    ]
