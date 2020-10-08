from django.conf.urls import url
from ProfileApp import views
from UserApp import user

urlpatterns=[
    url(r'^profile/$', views.profileApi),
]