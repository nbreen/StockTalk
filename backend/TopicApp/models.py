from django.db import models

# Create your models here.
class Topic(models.Model):
    TopicName = models.CharField(primary_key=True, max_length=64)
    IsStock = models.BooleanField(default=True)
    isTrending = models.BooleanField(default=False)
    TrendingScore = models.FloatField()
    NumberOfPosts = models.IntegerField()

    #TimeOfLastPost = models.IntegerField()
    #PreviousMA = models.IntegerField()
    #CurrentMA = models.IntegerField()
