from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http.response import JsonResponse
from django.core import serializers

from PostApp.serializers import PostSerializer
from PostApp.models import Post

from ProfileApp.serializers import ProfileSerializer
from ProfileApp.models import Profiles

from django.core.files.storage import default_storage

import ipdb;
from django.db import connection

# Create your views here.

class ProfileList(generics.ListAPIView):    
    serializer_class = ProfileSerializer

    def get_queryset(self):
        #ipdb.set_trace()
        profile_username = self.kwargs['username']
        return Profiles.objects.filter(Username=profile_username)
        


        


@csrf_exempt
def SaveProfilePic(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)

@csrf_exempt
def profileApi(request,id=0):

    if request.method=='GET':
        profiles = Profiles.objects.all()
        profile_serializer = ProfileSerializer(profiles, many=True)
        return JsonResponse(profile_serializer.data, safe=False)
        
    elif request.method=='POST':
        profile_data = JSONParser().parse(request)
        profile_serializer = ProfileSerializer(data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse("Profile added successfully", safe=False)
        return JsonResponse("Failed to add user", safe=False)

    elif request.method=='PUT':
        profile_data = JSONParser().parse(request)
        profile = Profiles.objects.get(Username=profile_data['Username'])
        profile_serializer = ProfileSerializer(profile, data=profile_data) 
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse("Profile updated successfully", safe=False)
        return JsonResponse("Failed to update profile", safe=False)

    elif request.method=='DELETE':
        profile=Profile.objects.get(Username=id)
        profile.delete()
        return JsonResponse("Deleted profile sucessfully", safe=False)    


@csrf_exempt
def getFollowers(request):
    name = str(request)[30:-2]
    # print(name)
    query = f'SELECT * FROM UserFollowsUser WHERE BeingFollowed = \"{name}\";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def getFollowing(request):
    name = str(request)[30:-2]
    # print(name)
    query = f'SELECT * FROM UserFollowsUser WHERE DoingFollowing = \"{name}\";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def getTopics(request):
    name = str(request)[36:-2]
    # print(name)

    query = f'SELECT * FROM UserFollowsTopic WHERE Username = \"{name}\";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def getButton(request):
    name = str(request).split("/")
    name1 = name[2]
    name2 = (name[3])[:-2]
    print(name1)
    print(name2)

    if name1 == name2:
        return JsonResponse("same", safe=False)


    query = f'SELECT * FROM UserFollowsUser WHERE DoingFollowing = \"{name1}\" AND BeingFollowed = \"{name2}\";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    # print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def followuser(request):
    name = str(request).split("/")
    name1 = name[2]
    name2 = (name[3])[:-2]
    print(name1)
    print(name2)

    query = f'INSERT INTO UserFollowsUser VALUES(\"{name1}\", \"{name2}\"); SET SQL_SAFE_UPDATES = 0; UPDATE UserApp_users SET Following=Following+1 WHERE Username = "{name1}"; UPDATE UserApp_users SET Followers=Followers+1 WHERE Username = "{name2}"; SET SQL_SAFE_UPDATES = 1;'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    # print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def unfollowuser(request):
    #print(str(request))
    name = str(request).split("/")
    name1 = name[2]
    name2 = (name[3])[:-2]
    #print(name1)
    print(name2)

    query = f'SET SQL_SAFE_UPDATES = 0; DELETE FROM UserFollowsUser WHERE DoingFollowing = \"{name1}\" AND BeingFollowed = \"{name2}\"; UPDATE UserApp_users SET Following=Following-1 WHERE Username = "{name1}"; UPDATE UserApp_users SET Followers=Followers-1 WHERE Username = "{name2}"; SET SQL_SAFE_UPDATES = 1;'
    cursor = connection.cursor()
    cursor.execute(query)
    #connection.commit()
    cursor.close()
    return JsonResponse("success", safe=False)

