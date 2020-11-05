
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http.response import JsonResponse
from django.core import serializers

from PostsApp.serializers import PostsSerializer
from PostsApp.models import Posts

from django.core.files.storage import default_storage

import ipdb;
from django.db import connection

# Create your views here.
@csrf_exempt
def getSavedPost(Method):
    # request = (str(Method)).split("/")
    # Username = (str(request[3]))[:-2]
    # print(Username)
    # post = Post.objects.filter(Username=Username)

    # post_serializer = PostSerializer(post, many=True)
    # print(post_serializer)
    # return JsonResponse(post_serializer.data, safe=False)


    request = (str(Method)).split("/")
    Username = (str(request[3]))[:-2]
    print(Username)
    query = f'SELECT PostId FROM UserSavesPost WHERE Username = "{Username}";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    print(records)
    cursor.close()
    # post_serializer = PostSerializer(records, many=True)
    # print(post_serializer)
    return JsonResponse(records, safe=False)


# Create your views here.
def getAllPosts(Method):
    post = Posts.objects.all()
    print(post)
    posts_serializer = PostsSerializer(post, many=True)
    print(posts_serializer)
    return JsonResponse(posts_serializer.data, safe=False)

@csrf_exempt
def getPost(Method):
    print(str(Method))
    request = (str(Method)).split("/")
    filterBy = request[2]
    mustEqual = (request[3])[:-2]
    #print()
    #print(filterBy)
    #print(mustEqual)

    post = "Hello"
    if (filterBy == "ByTopic"):
        post = Posts.objects.all().filter(TopicName=mustEqual)
        print(post)
    elif (filterBy == "ByUser"):
        post = Posts.objects.all().filter(Username=mustEqual)


    # post = Post.objects.all().filter(TopicName=topicname)

    print(post)
    posts_serializer = PostsSerializer(post, many=True)
    print(posts_serializer)
    return JsonResponse(posts_serializer.data, safe=False)


@csrf_exempt
def checkSavedPost(Method):
    print(str(Method))
    request = (str(Method)).split("/")
    Username = request[2]
    PostId = (request[3])[:-2]

    query = f'SELECT * FROM UserSavesPost WHERE Username = "{Username}" AND PostId = "{PostId}";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def savePost(request):
    name = str(request).split("/")
    Username = name[2]
    PostId = (name[3])[:-2]
    #print(Username)
    #print(PostId)

    query = f'INSERT INTO UserSavesPost VALUES(\"{Username}\", \"{PostId}\");'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    # print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def unsavePost(request):
    name = str(request).split("/")
    Username = name[2]
    PostId = (name[3])[:-2]
    #print(Username)
    #print(PostId)

    query = f'SET SQL_SAFE_UPDATES = 0; DELETE FROM UserSavesPost WHERE Username = \"{Username}\" AND PostId = \"{PostId}\"; SET SQL_SAFE_UPDATES = 1;'
    cursor = connection.cursor()
    cursor.execute(query)
    #connection.commit()
    cursor.close()
    return JsonResponse("success", safe=False)


@csrf_exempt
def postApi(request, id=0):


    if request.method=='GET':
        post = Post.objects.all()
        post_serializer = PostsSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)

    elif request.method=='POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostsSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Post added successfully", safe=False)
        return JsonResponse("Failed to add post", safe=False)

    elif request.method=='PUT':
        post_data = JSONParser().parse(request)
        post = Posts.objects.get(Username=user_data['Username'])
        post_serializer = PostsSerializer(post, data=post_data) 
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Post updated successfully", safe=False)
        return JsonResponse("Failed to update post", safe=False)

    elif request.method=='DELETE':
        post=Posts.objects.get(UserID="test")
        post.delete()
        return JsonResponse("Deleted post sucessfully", safe=False)   

