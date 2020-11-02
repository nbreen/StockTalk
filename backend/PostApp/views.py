from django.shortcuts import render

# Create your views here.
@csrf_exempt
def postApi(request,id=0):

    elif request.method=='POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Post added successfully", safe=False)
        return JsonResponse("Failed to add post", safe=False)

    elif request.method=='DELETE':
        post=Post.objects.get(UserID=id)
        user.delete()
        return JsonResponse("Deleted user sucessfully", safe=False)    