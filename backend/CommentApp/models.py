from django.db import models

# Create your models here.

class Comment(models.Model):
    CommentId = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=64)
    PostId = models.IntegerField(default=0)
    Comment = models.CharField(max_length=256, default='')
    CommentDate = models.CharField(max_length=256, default='')


