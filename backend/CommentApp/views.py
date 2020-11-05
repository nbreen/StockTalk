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

    comment = Comment.objects.all().filter(PostId=mustEqual)
    
    print(comment)
    comment_serializer = CommentSerializer(comment, many=True)
    print(comment_serializer)
    return JsonResponse(comment_serializer.data, safe=False)

