# Generated by Django 4.0.3 on 2022-05-17 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0004_alter_blog_autor_alter_blog_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Fecha',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
