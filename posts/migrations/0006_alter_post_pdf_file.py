# Generated by Django 5.1.1 on 2024-10-17 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pdf_file',
            field=models.FileField(upload_to=''),
        ),
    ]
