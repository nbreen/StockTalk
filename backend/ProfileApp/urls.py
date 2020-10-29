from django.conf.urls import url
from ProfileApp import views

urlpatterns=[
    url(r'^profile/$', views.profileApi),
    url(r'^profile/(?P<username>.+)/$', views.ProfileList.as_view()),
]