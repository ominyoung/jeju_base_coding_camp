# Generated by Django 3.1 on 2022-08-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_cafe_subphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='insta',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='cafe',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]