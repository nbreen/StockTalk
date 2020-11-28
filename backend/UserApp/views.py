from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connection
from rest_framework import generics
from django.conf import settings
import bcrypt

from UserApp.models import Users
from UserApp.serializers import UserSerializer
from UserApp.serializers import FollowTopicSerializer
import re

# Create your views here.

class UserList(generics.ListAPIView):    
    serializer_class = UserSerializer

    def get_queryset(self):
        #ipdb.set_trace()
        username = self.kwargs['username']
        return Users.objects.filter(Username=username)


@csrf_exempt
def userDeleteApi(id):
    name = (str(id)[35:-2])
    print(name)
    ### Manually deleting a user's account and their related data. Done manually because Models and schema do not implement ON DELETE CASCADE
    query = f'DELETE FROM UserApp_users WHERE Username = \"{name}\"; DELETE FROM PostsApp_posts WHERE Username = "{name}"; DELETE FROM UserFollowsUser WHERE DoingFollowing = "{name}" OR BeingFollowed = "{name}"; DELETE FROM UserFollowsTopic WHERE Username = "{name}"; DELETE FROM UserSavesPost WHERE Username = "{name}";'
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    return JsonResponse("Deleted user sucessfully", safe=False)

@csrf_exempt
def suggestedTopics(request):
    name = str(request).split("/")
    currUser = (name[2])[:-2]

    query = f'SELECT * FROM RecommendTopics WHERE CurrentUser = "{currUser}" ORDER BY -Score, RecommendedTopic LIMIT 0, 10;'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def suggestedUsers(request):
    name = str(request).split("/")
    currUser = (name[2])[:-2]

    query = f'SELECT * FROM RecommendUsers WHERE CurrentUser = "{currUser}" ORDER BY -Score, RecommendedUser LIMIT 0, 10;'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def userApi(request,id=0):

    if request.method=='GET':
        user = Users.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if (set(user_data['Password'])-set(user_data['Password'].lower())==set() and set(user_data['Password'])-set(user_data['Password'].upper())==set()):
            return JsonResponse("Error: Your password is invalid! Make sure there is one upper and one lowercase letter.",
                safe=False)
        if user_serializer.is_valid() and int(user_data['UserAge']) >= 18 and set(user_data['Password'])-set(user_data['Password'].lower())!=set() and set(user_data['Password'])-set(user_data['Password'].upper())!=set():
            passwd = user_data['Password']
            passwd = bytes(passwd, 'utf-8')
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(passwd, salt)
            user_data['Password'] = str(hashed)
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse("User added successfully", safe=False)
        if (int(user_data['UserAge']) < 18):
            return JsonResponse("Error: You must be 18 or older to create an account!",
                safe=False)
       
        print(user_serializer.errors)
        return JsonResponse("Failed to add user", safe=False)

    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(Username=user_data['Username'])
        user_serializer = UserSerializer(user, data=user_data) 
        if user_serializer.is_valid():
            passwd = user_data['Password']
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(passwd, salt)
            user_data['Password'] = str(hashed)
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse("User added successfully", safe=False)
        return JsonResponse("Failed to update user", safe=False)

    elif request.method=='DELETE':
        user=Users.objects.get(UserID=id)
        user.delete()
        return JsonResponse("Deleted user sucessfully", safe=False)    
    
@csrf_exempt    
def followTopicApi(request, id, fol):
    if request.method=='GET':
        value = UserFollowsTopic.objects.all()
        follow_serializer = FollowTopicSerializer(value, many=True)
        return JsonResponse(follow_serializer.data, safe=False)

    elif request.method=='POST':
        follow_data = JSONParser().parse(request)
        follow_serializer = FollowTopicSerializer(data=follow_data)
        if follow_serializer.is_valid():
            follow_serializer.save()
            return JsonResponse("User followed successfully", safe=False)
        print(follow_serializer.errors)
        return JsonResponse("Failed to follow user", safe=False)

    elif request.method=='DELETE':
        value=UserFollowsTopic.objects.get(UserID=id, TopicFollowed=fol)
        value.delete()
        return JsonResponse("User unfollowed sucessfully", safe=False)
