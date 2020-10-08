from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import Profiles
from UserApp.serializers import UserSerializer

# Create your views here.
@csrf_exempt
def profileApi(request,id=0):

    if request.method=='GET':
        profile = Profiles.objects.all()
        profile_serializer = ProfileSerializer(profile, many=True)
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