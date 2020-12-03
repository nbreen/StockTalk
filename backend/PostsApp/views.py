
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http.response import JsonResponse
from django.core import serializers

from PostsApp.serializers import PostsSerializer
from PostsApp.models import Posts

from django.core.files.storage import default_storage

import ipdb;
from django.db import connection

# Advanced
from StockTalk.advanced_functionality.recommendTopics import update as updateTopics
# End Advanced

# Create your views here.
@csrf_exempt
def getSavedPost(Method):
    # request = (str(Method)).split("/")
    # Username = (str(request[3]))[:-2]
    # print(Username)
    # post = Post.objects.filter(Username=Username)

    # post_serializer = PostSerializer(post, many=True)
    # print(post_serializer)
    # return JsonResponse(post_serializer.data, safe=False)


    request = (str(Method)).split("/")
    Username = (str(request[3]))[:-2]
    print(Username)
    query = f'SELECT PostId FROM UserSavesPost WHERE Username = "{Username}" ORDER BY "PostId" DESC;'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    print(records)
    cursor.close()
    # post_serializer = PostSerializer(records, many=True)
    # print(post_serializer)
    return JsonResponse(records, safe=False)


# Create your views here.
def getAllPosts(Method):
    post = Posts.objects.all()
    print(post)
    posts_serializer = PostsSerializer(post, many=True)
    print(posts_serializer)
    return JsonResponse(posts_serializer.data, safe=False)

@csrf_exempt
def getPost(Method):
    print(str(Method))
    request = (str(Method)).split("/")
    filterBy = request[2]
    mustEqual = (request[3])[:-2]
    #print()
    #print(filterBy)
    #print(mustEqual)

    if (filterBy == "ByTopic"):
        post = Posts.objects.all().filter(TopicName=mustEqual).order_by('-PostId')
        print(post)
    elif (filterBy == "ByUser"):
        post = Posts.objects.all().filter(Username=mustEqual).order_by('-PostId')
    elif (filterBy == "ById"):
        post = Posts.objects.all().filter(PostId=mustEqual)
    elif (filterBy == "ByArray"):
        mustEqual = mustEqual.split(",")
        print(mustEqual)
        post = Posts.objects.all().filter(PostId__in=mustEqual).order_by('-PostId')



    # post = Post.objects.all().filter(TopicName=topicname)

    print(post)
    posts_serializer = PostsSerializer(post, many=True)
    print(posts_serializer)
    return JsonResponse(posts_serializer.data, safe=False)

@csrf_exempt
def getFollowingPostId(Method):

    request = (str(Method)).split("/")
    Username = (str(request[2]))[:-2]
    print(Username)
    query = f'''SELECT * FROM
        (SELECT PostId FROM PostsApp_posts p
        JOIN (SELECT * FROM UserFollowsUser WHERE DoingFollowing = '{Username}') s
        ON p.Username = s.BeingFollowed
        UNION
        SELECT PostId
        FROM PostsApp_posts p
        JOIN (SELECT * FROM UserFollowsTopic WHERE Username = '{Username}') t
        ON p.TopicName = t.TopicName) T1 ORDER BY PostId DESC;'''
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    print(records)
    cursor.close()
    # post_serializer = PostSerializer(records, many=True)
    # print(post_serializer)
    return JsonResponse(records, safe=False)

@csrf_exempt
def checkSavedPost(Method):
    #print(str(Method))
    request = (str(Method)).split("/")
    Username = request[2]
    PostId = (request[3])[:-2]

    query = f'SELECT * FROM UserSavesPost WHERE Username = "{Username}" AND PostId = "{PostId}"'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    #print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def savePost(request):
    name = str(request).split("/")
    Username = name[2]
    PostId = (name[3])[:-2]
    #print(Username)
    #print(PostId)

    query = f'INSERT INTO UserSavesPost VALUES(\"{Username}\", \"{PostId}\");'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    # print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def unsavePost(request):
    name = str(request).split("/")
    Username = name[2]
    PostId = (name[3])[:-2]
    #print(Username)
    #print(PostId)

    query = f'SET SQL_SAFE_UPDATES = 0; DELETE FROM UserSavesPost WHERE Username = \"{Username}\" AND PostId = \"{PostId}\"; SET SQL_SAFE_UPDATES = 1;'
    cursor = connection.cursor()
    cursor.execute(query)
    #connection.commit()
    cursor.close()
    return JsonResponse("success", safe=False)

# Votes Stuff
@csrf_exempt
def checkVotes(Method):
    print(str(Method))
    request = (str(Method)).split("/")
    Username = request[2]
    PostId = (request[3])[:-2]

    query = f'SELECT * FROM PostVotes WHERE Username = "{Username}" AND PostId = "{PostId}";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def deleteVote(Method):
    print(str(Method))
    request = (str(Method)).split("/")
    Username = request[2]
    PostId = (request[3])[:-2]

    query = f'DELETE FROM PostVotes WHERE Username = "{Username}" AND PostId = "{PostId}";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def upvote(Method):
    print(str(Method))
    request = (str(Method)).split("/")
    Username = request[2]
    PostId = (request[3])[:-2]

    query = f'DELETE FROM PostVotes WHERE Username = "{Username}" AND PostId = "{PostId}"; INSERT INTO PostVotes VALUES("{Username}", {PostId}, 1);'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def downvote(Method):
    print(str(Method))
    request = (str(Method)).split("/")
    Username = request[2]
    PostId = (request[3])[:-2]

    query = f'DELETE FROM PostVotes WHERE Username = "{Username}" AND PostId = "{PostId}"; INSERT INTO PostVotes VALUES("{Username}", {PostId}, -1);'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)

@csrf_exempt
def addvotes(Method):
    request = (str(Method)).split("/")
    PostId = (request[2])[:-2]
    print(PostId)

    query = f'SELECT SUM(Vote) FROM PostVotes WHERE PostId = "{PostId}";'
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    print(records)
    cursor.close()
    return JsonResponse(records, safe=False)


@csrf_exempt
def postApi(request, id=0):


    if request.method=='GET':
        post = Post.objects.all()
        post_serializer = PostsSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)

    elif request.method=='POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostsSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()

            # Advanced
            username = post_data['Username']
            topicname = post_data['TopicName']
            newPostInt = 0
            updateTopics(username, topicname, newPostInt) # Does things for RecommendTopics
            # End Advanced

            return JsonResponse("Post added successfully", safe=False)
        return JsonResponse("Failed to add post", safe=False)

    elif request.method=='PUT':
        #ipdb.set_trace()
        post_data = JSONParser().parse(request)
        post = Posts.objects.get(TopicName=post_data['TopicName'])
        post_serializer = PostsSerializer(post, data=post_data) 
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Post updated successfully", safe=False)
        return JsonResponse("Failed to update post", safe=False)

    elif request.method=='DELETE':
        post=Posts.objects.get(UserID="test")
        post.delete()
        return JsonResponse("Deleted post sucessfully", safe=False)


@csrf_exempt
def suggestTopics(Method):
    methString = str(Method)[-3]

    if int(methString) == 0 :
        topic = Topic.objects.all().filter(isTrending=1).only('TopicName',
                        'IsStock',
                        'isTrending',
                        'TrendingScore',
                        'NumberOfPosts').order_by("-TrendingScore", "TopicName")
    print(topic)
    topic_serializer = TopicSerializer(topic, many=True)
    print(topic_serializer)
    return JsonResponse(topic_serializer.data, safe=False)


@csrf_exempt
def SavePostPic(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


