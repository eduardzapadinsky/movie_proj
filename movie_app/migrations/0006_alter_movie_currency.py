# Generated by Django 4.0.6 on 2022-08-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('USD', 'Dollar'), ('EUR', 'Euro'), ('UAH', 'Uah')], default='UAH', max_length=3),
        ),
    ]
