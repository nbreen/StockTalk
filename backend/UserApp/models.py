from django.db import models

# Create your models here.

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    DateOfJoining = models.DateTimeField()
    UserAge = models.IntegerField(min_value = 13)
