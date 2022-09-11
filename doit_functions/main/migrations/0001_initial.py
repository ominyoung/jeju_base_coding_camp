# Generated by Django 3.1 on 2022-08-29 00:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('created_date', models.DateField()),
                ('modified_date', models.DateField()),
                ('star', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('companyName', models.CharField(max_length=40)),
                ('licenseDate', models.CharField(max_length=30)),
            ],
        ),
    ]