from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import Users
import bcrypt
#from UserApp.views import salt
salt = b'$2b$12$7KcY5oHPhABt0RDOdNKjdu'

# Create your views here.
@csrf_exempt
def loginApi(request,id=0):

    if request.method=='POST':
        user_data = JSONParser().parse(request)
        print(salt)
        print(user_data['Password'])

        passwd = user_data['Password']
        passwd = bytes(passwd, 'utf-8')
        hashed = bcrypt.hashpw(passwd, salt)
        user_data['Password'] = str(hashed)
        print(user_data['Password'])



        existing_user = Users.objects.filter(Username=user_data['Username'])
        if existing_user:
            return JsonResponse("User exists", safe=False)
        else:    
            return JsonResponse("User does not exist", safe=False)

@csrf_exempt
def hashPassword(request):
    name = str(request).split("/")
    name1 = (name[2])[:-2]
    passwd = name1
    passwd = bytes(passwd, 'utf-8')
    hashed = str(bcrypt.hashpw(passwd, salt))
    print(hashed)
    return JsonResponse(hashed, safe=False)