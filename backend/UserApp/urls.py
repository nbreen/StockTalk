from django.conf.urls import url
from UserApp import views

urlpatterns=[
    url(r'^user/$', views.userApi),
    url(r'^user/([0-9]+)$', views.userApi),
    url(r'^delete-user\/.*$', views.userDeleteApi)
]