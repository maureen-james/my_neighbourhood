# Generated by Django 4.0.5 on 2022-06-17 13:38

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Profile Image')),
                ('bio', models.TextField(max_length=300)),
                ('location', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.CharField(blank=True, max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
