# Generated by Django 4.0.3 on 2022-05-17 00:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0002_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2022, 5, 16, 21, 34, 27, 185499)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/blog'),
        ),
    ]
