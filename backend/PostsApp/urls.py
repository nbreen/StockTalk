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
    url(r'^posts/$', views.postApi),
    url(r'^checkvotes\/.*$', views.checkVotes),
    url(r'^deletevote\/.*$', views.deleteVote),
    url(r'^upvote\/.*$', views.upvote),
    url(r'^downvote\/.*$', views.downvote),
    url(r'^addvotes\/.*$', views.addvotes),
    url(r'^suggestTopics/.$', views.suggestTopics)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
