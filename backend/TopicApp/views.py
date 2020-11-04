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


@csrf_exempt
def getButton(request):
    name = str(request).split("/")
    name1 = name[2]
    name2 = (name[3])[:-2]
    print(name1)
    print(name2)

    query = f'SELECT * FROM UserFollowsTopic WHERE Username = \"{name1}\" AND TopicName = \"{name2}\";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    # print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def followtopic(request):
    #print(str(request))
    name = str(request).split("/")
    name1 = name[2]
    name2 = (name[3])[:-2]
    #print(name1)
    #print(name2)

    query = f'INSERT INTO UserFollowsTopic VALUES(\"{name1}\", \"{name2}\");'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    # print(records)
    cursor.close()
    return JsonResponse(records, safe=False)
    
@csrf_exempt
def unfollowtopic(request):
    print(str(request))
    name = str(request).split("/")
    name1 = name[2]
    name2 = (name[3])[:-2]
    #print("WE ARE DELETING THIS PAIR")
    #print(name1)
    #print(name2)

    queryDel = f'SET SQL_SAFE_UPDATES = 0; DELETE FROM UserFollowsTopic WHERE Username = \"{name1}\" AND TopicName = \"{name2}\"; SET SQL_SAFE_UPDATES = 1;'
    cursor = connection.cursor()
    cursor.execute(queryDel)
    records = cursor.fetchall()
    # connection.commit()
    cursor.close()
    return JsonResponse(records, safe=False)
