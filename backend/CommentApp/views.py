from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http.response import JsonResponse
from django.core import serializers

from CommentApp.serializers import CommentSerializer
from CommentApp.models import Comment

from django.core.files.storage import default_storage

import ipdb;
from django.db import connection

# Create your views here.
@csrf_exempt
def getComments(Method):
    print(str(Method))
    request = (str(Method)).split("/")
    mustEqual = (request[2])[:-2]
    print(mustEqual)

    comment = Comment.objects.all().filter(PostId=mustEqual).order_by('-CommentId')
    
    print(comment)
    comment_serializer = CommentSerializer(comment, many=True)
    print(comment_serializer)
    return JsonResponse(comment_serializer.data, safe=False)

@csrf_exempt
def commentApi(request, id=0):
    post_data = JSONParser().parse(request)
    post_serializer = CommentSerializer(data=post_data)
    if post_serializer.is_valid():
        post_serializer.save()

        return JsonResponse("Comment added successfully", safe=False)
    return JsonResponse("Failed to add comment", safe=False)
