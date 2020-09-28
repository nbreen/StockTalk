# Generated by Django 3.1.1 on 2020-09-28 22:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='UserEmail',
            new_name='Email',
        ),
        migrations.AddField(
            model_name='users',
            name='DateOfJoining',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='Password',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
