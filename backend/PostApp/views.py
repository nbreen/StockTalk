from django.shortcuts import render

# Create your views here.
@csrf_exempt
def userApi(request,id=0):

    if request.method=='GET':
        post = Post.objects.all()
        post_serializer = PostSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)

    elif request.method=='POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Post added successfully", safe=False)
        return JsonResponse("Failed to add post", safe=False)

    elif request.method=='PUT':
        post_data = JSONParser().parse(request)
        post = Post.objects.get(Username=user_data['Username'])
        post_serializer = PostSerializer(post, data=post_data) 
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Post updated successfully", safe=False)
        return JsonResponse("Failed to update post", safe=False)

    elif request.method=='DELETE':
        post=Post.objects.get(UserID=id)
        post.delete()
        return JsonResponse("Deleted post sucessfully", safe=False)   


