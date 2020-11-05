from django.conf.urls import url
from CommentApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^getComments/.*$', views.getComments),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)