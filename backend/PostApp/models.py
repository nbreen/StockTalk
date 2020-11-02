from django.db import models

# Create your models here.

class Post(models.Model):
    PostID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=64)
    Text = models.CharField(max_length=256, default='')
    Image = models.CharField(max_length=256, default='')
    Topic = models.CharField(max_length=256, default='')
    Upvotes = models.IntegerField(default=0)
    Downvotes = models.IntegerField(default=0)
