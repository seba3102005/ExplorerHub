# Generated by Django 5.1.5 on 2025-02-18 19:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default_blog_photo_hihiym', max_length=255, verbose_name='image'),
        ),
    ]
