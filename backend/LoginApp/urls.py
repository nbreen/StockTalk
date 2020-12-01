from django.conf.urls import url
from LoginApp import views

urlpatterns=[
    url(r'^login/$', views.loginApi),
    url(r'^hashPassword/.*$', views.hashPassword)
]