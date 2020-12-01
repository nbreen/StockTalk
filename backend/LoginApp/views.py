from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import Users


# Create your views here.
@csrf_exempt
def loginApi(request,id=0):

    if request.method=='POST':
        user_data = JSONParser().parse(request)
        existing_user = Users.objects.filter(Username=user_data['Username'])
        if existing_user:
            return JsonResponse("User exists", safe=False)
        else:    
            return JsonResponse("User does not exist", safe=False)
    elif request.method=='PUT':
            passwd = JSONParser().parse(request)
            hash = bcrypt.hashpw(passwd, salt)
            return str(hash)
