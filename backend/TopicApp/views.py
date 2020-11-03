from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from django.db import connection

from TopicApp.models import Topic
from TopicApp.serializers import TopicSerializer
import re

# Create your views here.
@csrf_exempt
def getAllTopics(Method):
    methString = str(Method)[-3]

    if int(methString) == 0 :
        topic = Topic.objects.all().only('TopicName',
                        'IsStock',
                        'isTrending',
                        'TrendingScore',
                        'NumberOfPosts').order_by("TopicName")
    elif int(methString) == 1 :
        topic = Topic.objects.all().only('TopicName',
                        'IsStock',
                        'isTrending',
                        'TrendingScore',
                        'NumberOfPosts').order_by("-NumberOfPosts", "TopicName")
    elif int(methString) == 2 :
        topic = Topic.objects.all().filter(isTrending=1).only('TopicName',
                        'IsStock',
                        'isTrending',
                        'TrendingScore',
                        'NumberOfPosts').order_by("-TrendingScore", "TopicName")
    print(topic)
    topic_serializer = TopicSerializer(topic, many=True)
    print(topic_serializer)
    return JsonResponse(topic_serializer.data, safe=False)



def getTrendingTopics(TopicName):
    topic = Topic.objects.all().filter(isTrending=1).only('TopicName',
                        'IsStock',
                        'isTrending',
                        'TrendingScore',
                        'NumberOfPosts')
    print(topic)
    topic_serializer = TopicSerializer(topic, many=True)
    print(topic_serializer)
    return JsonResponse(topic_serializer.data, safe=False)
