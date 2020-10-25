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
def getAllTopics(Topic):
    # all_topics = Topic.objects.all()
    return JsonResponse("Test", safe=False)