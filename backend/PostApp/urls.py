from django.conf.urls import url
from PostApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^getPost\/.*$', views.getPost),
    url(r'^checksavedpost\/.*$', views.checkSavedPost),
    url(r'^unsavepost\/.*$', views.unsavePost),
    url(r'^savepost\/.*$', views.savePost)


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
