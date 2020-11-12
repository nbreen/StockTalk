# Generated by Django 3.1.1 on 2020-11-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('CommentId', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=64)),
                ('PostId', models.IntegerField(default=0)),
                ('Comment', models.CharField(default='', max_length=256)),
                ('CommentDate', models.CharField(default='', max_length=256)),
            ],
        ),
    ]