from django.db import models

# Create your models here.

class Comment(models.Model):
    Username = models.CharField(max_length=64)
    TextField = models.CharField(max_length=256, default='')
    Upvotes = models.IntegerField(default=0)
    Downvotes = models.IntegerField(default=0)

