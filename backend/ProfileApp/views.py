from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http.response import JsonResponse

from ProfileApp.serializers import ProfileSerializer
from ProfileApp.models import Profiles

from django.core.files.storage import default_storage

# Create your views here.

class ProfileList(generics.ListAPIView):    
    serializer_class = ProfileSerializer

    def get_queryset(self):
        profile_username = self.kwargs['username']
        return Profiles.objects.filter(Username = profile_username)


@csrf_exempt
def SaveProfilePic(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)

@csrf_exempt
def profileApi(request,id=0):
        

    if request.method=='POST':
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
