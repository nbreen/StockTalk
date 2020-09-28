from django.db import models

# Create your models here.

class Users(models.Model):
    Username = models.CharField(max_length=100)
    UserEmail = models.CharField(max_length=100)
    UserID = models.AutoField(primary_key=True)
