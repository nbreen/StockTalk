from django.conf.urls import url
from TopicApp import views

urlpatterns=[
    url(r'^topic/.$', views.getAllTopics),
    url(r'checkfollowtopic/.*$', views.getButton),
    url(r'unfollowtopic/.*$', views.unfollowtopic),
    url(r'followtopic/.*$', views.followtopic),
    url(r'suggestTopics/.*$', views.suggestTopics),
    url(r'getTopicCount/$', views.getTopicCount)
]
