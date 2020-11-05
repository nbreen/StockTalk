from django.shortcuts import render
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http.response import JsonResponse
from django.core import serializers
from CommentApp import views

from CommentApp.serializers import CommentSerializer
from CommentApp.models import Comment


from django.core.files.storage import default_storage

import ipdb;
from django.db import connection

urlpatterns=[
    url(r'^comment/$', views.commentApi),
]