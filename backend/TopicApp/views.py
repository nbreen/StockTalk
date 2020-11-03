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
def getAllTopics(TopicName):
    topic = Topic.objects.all().only('TopicName',
                    'IsStock',
                    'isTrending',
                    'TrendingScore',
                    'NumberOfPosts')
    # print(topic)
    topic_serializer = TopicSerializer(topic, many=True)
    # print(topic_serializer)
    return JsonResponse(topic_serializer.data, safe=False)