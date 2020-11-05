from django.db import models

# Create your models here.

class Post(models.Model):
    Username = models.CharField(default='', max_length=256)
    PostId = models.AutoField(primary_key=True)
    UserId = models.IntegerField(default=0)
    TopicName = models.CharField(max_length=256, default='')
    PostType = models.IntegerField(default=0)
    Post = models.CharField(max_length=256, default='')
    PostDate = models.CharField(max_length=256, default='')
    Downvotes = models.IntegerField(default=0)
    Upvotes = models.IntegerField(default=0)
    Anonymous = models.IntegerField(default=0)
    PostImage = models.CharField(default='',max_length=256)
