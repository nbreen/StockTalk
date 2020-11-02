from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import connection
from rest_framework import generics

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
    newid = re.findall("\d+", str(id))[0]
    query = "DELETE FROM UserApp_users WHERE UserID = " + newid
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()

    return JsonResponse("Deleted user sucessfully", safe=False)

@csrf_exempt
def userApi(request,id=0):

    if request.method=='GET':
        user = Users.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid() and int(user_data['UserAge']) >= 18:
            user_serializer.save()
            return JsonResponse("User added successfully", safe=False)
        if (int(user_data['UserAge']) < 18):
            return JsonResponse("Error: You must be 18 or older to create an account!",
                safe=False)
        if (set(user_data['Password'])-set(user_data['Password'].lower())!=set() and set(user_data['Password'])-set(user_data['Password'].upper())!=set()):
            return JsonResponse("Error: Your password is invalid! Make sure there is one upper and one lowecase letter.",
                safe=False)
        print(user_serializer.errors)
        return JsonResponse("Failed to add user", safe=False)

    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(UserID=user_data['UserID'])
        user_serializer = UserSerializer(user, data=user_data) 
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("User updated successfully", safe=False)
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
