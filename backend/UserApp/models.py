from django.db import models

# Create your models here.

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=64)
    FullName = models.CharField(max_length=64, default='')
    Email = models.CharField(max_length=64)
    Password = models.CharField(max_length=64)
    UserAge = models.IntegerField(default=0)


