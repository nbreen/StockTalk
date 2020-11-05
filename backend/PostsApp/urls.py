from django.conf.urls import url
from PostsApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^addPosts/$', views.postApi),
    url(r'^getPost/BySaved/.*$', views.getSavedPost),
    url(r'^getPost\/.*$', views.getPost),
    url(r'^checksavedpost\/.*$', views.checkSavedPost),
    url(r'^unsavepost\/.*$', views.unsavePost),
    url(r'^savepost\/.*$', views.savePost),
    url(r'^getAllPosts\/.*$', views.getAllPosts),
    url(r'^addPost/$', views.postApi)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
