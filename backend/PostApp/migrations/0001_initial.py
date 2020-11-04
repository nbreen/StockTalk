# Generated by Django 3.1.1 on 2020-11-03 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=64)),
                ('Text', models.CharField(default='', max_length=256)),
                ('Image', models.CharField(default='', max_length=256)),
                ('Topic', models.CharField(default='', max_length=256)),
                ('Upvotes', models.IntegerField(default=0)),
                ('Downvotes', models.IntegerField(default=0)),
            ],
        ),
    ]
