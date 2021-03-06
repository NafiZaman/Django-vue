# Generated by Django 3.1.2 on 2022-01-02 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtime', '0003_auto_20220102_1232'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='showtime',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='showtime',
            constraint=models.UniqueConstraint(fields=('movie', 'theatre'), name='showtime'),
        ),
    ]
