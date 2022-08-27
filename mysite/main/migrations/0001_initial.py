# Generated by Django 3.1 on 2022-08-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(choices=[('Hangyeong-myeon', '한경면'), ('Hallim-eup', '한림읍'), ('Aewol-eup', '애월읍'), ('Jeju-si', '제주시'), ('Jocheon-eup', '조천읍'), ('Gujwa-eup', '구좌읍'), ('Daejeong-eup', '대정읍'), ('Andeok-myeon', '안덕면'), ('Seogwipo-si', '서귀포시'), ('Namwon-eup', '남원읍'), ('Pyoseon-myeon', '표선면'), ('Seongsan-eup', '성산읍'), ('Udo-myeon', '우도면')], max_length=50)),
                ('content', models.TextField()),
                ('mainphoto', models.ImageField(blank=True, null=True, upload_to='')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
