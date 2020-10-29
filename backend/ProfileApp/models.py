from django.db import models

# Create your models here.

class Profiles(models.Model):
    Username = models.CharField(max_length=64)
    Bio = models.CharField(max_length=256, default='empty')
    ProfileImage = models.CharField(max_length=256, default='empty')
    