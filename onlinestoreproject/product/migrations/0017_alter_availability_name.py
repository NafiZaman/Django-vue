# Generated by Django 4.0.1 on 2022-02-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_rename_promos_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
