# Generated by Django 4.0.3 on 2022-05-17 13:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0003_alter_blog_fecha_alter_blog_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Autor',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='blog',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2022, 5, 17, 10, 58, 5, 665553)),
        ),
    ]