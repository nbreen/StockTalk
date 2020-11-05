from django.conf.urls import url
from PostsApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^addPosts/$', views.postApi)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
