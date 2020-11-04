from django.db import models

# Create your models here.

class Post(models.Model):
    PostId = models.IntegerField(default=0)
    UserID = models.IntegerField(default=0)
    TopicName = models.CharField(max_length=256, default='')
    PostType = models.IntegerField(default=0)
    Post = models.CharField(max_length=256, default='')
    PostDate = models.CharField(max_length=256, default='')
    Downvotes = models.IntegerField(default=0)
    Upvotes = models.IntegerField(default=0)
    Anonymous = models.IntegerField(default=0)
    PostImage = models.CharField(max_length=256, default='empty')
