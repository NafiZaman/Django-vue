# Generated by Django 3.1.2 on 2022-01-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='coming_soon',
            field=models.BooleanField(default=False),
        ),
    ]
