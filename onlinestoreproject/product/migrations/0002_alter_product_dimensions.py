# Generated by Django 4.0.1 on 2022-02-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dimensions',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
