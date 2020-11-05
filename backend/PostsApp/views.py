
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

