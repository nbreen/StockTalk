from django.db import models

# Create your models here.
class Topic(models.Model):
    TopicName = models.CharField(primary_key=True, max_length=64)
    IsStock = models.BooleanField(default=True)
    