from django.conf.urls import url
from ProfileApp import views

urlpatterns=[
    url(r'^profile\/.*$', views.profileApi),
]