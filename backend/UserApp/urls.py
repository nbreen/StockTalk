from django.conf.urls import url
from UserApp import views

urlpatterns=[
    url(r'^user/$', views.userApi),
    url(r'^user/(?P<username>.+)/$', views.UserList.as_view()),
    url(r'^delete-user\/.*$', views.userDeleteApi)
]