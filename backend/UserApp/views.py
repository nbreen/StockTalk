from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import Users
from UserApp.serializers import UserSerializer

# Create your views here.
@csrf_exempt
def userApi(request,id=0):

    if request.method=='GET':
        user = Users.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid() and user_data['UserAge'] >= 18:
            user_serializer.save()
            return JsonResponse("User added successfully", safe=False)
        if(user_data['UserAge'] < 18):
            print("Error: You must be 18 or older to create an account!")
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
