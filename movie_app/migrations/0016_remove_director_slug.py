# Generated by Django 4.0.6 on 2022-08-06 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_director_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='slug',
        ),
    ]
