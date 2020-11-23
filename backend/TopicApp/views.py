from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from urllib.parse import unquote
from django.db import connection

from TopicApp.models import Topic
from TopicApp.serializers import TopicSerializer
import re

# Advanced
from StockTalk.advanced_functionality.recommendTopics import update as updateTopics
from StockTalk.advanced_functionality.suggestTopics import update as updateSuggestedTopics
# End Advanced

# Create your views here.
@csrf_exempt
def getAllTopics(Method):
    print("***********************")
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
def suggestTopics(Method):
    print("***********************")
    args = str(Method).split("/")
    print(Method)
    user = args[3]
    postText = unquote(args[4])
    methString = str(args[2])
    print(args)
    #postText = "test placeholder #T"
    print(user)
    print(postText)
    print("***********************")

    if int(methString) == 0:
        suggestedTopics = updateSuggestedTopics(user, postText)
        topic = []
        for t in suggestedTopics:
            topic.append(Topic.objects.all().get(TopicName__exact=t))
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

    # Advanced
    followInt = 1
    updateTopics(name1, name2, followInt) # Does things for RecommendTopics
    # End Advanced

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
