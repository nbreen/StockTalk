from django.conf.urls import url
from UserApp import views

urlpatterns=[
    url(r'^posts/$', views.postApi),
]