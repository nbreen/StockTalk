# Generated by Django 3.1.1 on 2020-11-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('Username', models.CharField(max_length=64)),
                ('Bio', models.CharField(default='empty', max_length=256)),
                ('ProfileImage', models.CharField(default='empty', max_length=256)),
            ],
        ),
    ]
