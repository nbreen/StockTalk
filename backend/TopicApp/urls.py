from django.conf.urls import url
from TopicApp import views

urlpatterns=[
    url(r'^topic/.$', views.getAllTopics)
]