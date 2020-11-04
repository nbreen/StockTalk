from django.conf.urls import url
from PostApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^getPost\/.*$', views.getPostByTopic)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
