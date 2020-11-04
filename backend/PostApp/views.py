from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http.response import JsonResponse
from django.core import serializers

from PostApp.serializers import PostSerializer
from PostApp.models import Post

from django.core.files.storage import default_storage

import ipdb;
from django.db import connection


# Create your views here.
@csrf_exempt
def getPost(Method):
    print(str(Method))
    request = (str(Method)).split("/")
    filterBy = request[2]
    mustEqual = (request[3])[:-2]
    #print()
    #print(filterBy)
    #print(mustEqual)

    post = "Placeholder"

    if (filterBy == "ByTopic"):
        post = Post.objects.all().filter(TopicName=mustEqual)
    elif (filterBy == "ByUser"):
        post = Post.objects.all().filter(Username=mustEqual)


    # post = Post.objects.all().filter(TopicName=topicname)

    print(post)
    post_serializer = PostSerializer(post, many=True)
    print(post_serializer)
    return JsonResponse("Placeholder", safe=False)


@csrf_exempt
def userApi(request,id=0):

    if request.method=='GET':
        post = Post.objects.all()
        post_serializer = PostSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)

    elif request.method=='POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Post added successfully", safe=False)
        return JsonResponse("Failed to add post", safe=False)

    elif request.method=='PUT':
        post_data = JSONParser().parse(request)
        post = Post.objects.get(Username=user_data['Username'])
        post_serializer = PostSerializer(post, data=post_data) 
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Post updated successfully", safe=False)
        return JsonResponse("Failed to update post", safe=False)

    elif request.method=='DELETE':
        post=Post.objects.get(UserID=id)
        post.delete()
        return JsonResponse("Deleted post sucessfully", safe=False)   

