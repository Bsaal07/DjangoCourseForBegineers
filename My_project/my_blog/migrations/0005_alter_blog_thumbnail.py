# Generated by Django 5.1.4 on 2025-01-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_blog_views_alter_blog_thumbnail_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, default='img/profile.png', upload_to='uploads/blog_images/'),
        ),
    ]
