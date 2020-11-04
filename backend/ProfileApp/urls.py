from django.conf.urls import url
from ProfileApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^profile/$', views.profileApi),
    url(r'^profile/(?P<username>.+)/$', views.ProfileList.as_view()),
    url(r'^SaveProfilePic/$', views.SaveProfilePic),
    url(r'followers/.*$', views.getFollowers),
    url(r'following/.*$', views.getFollowing),
    url(r'topicsFollowing/.*$', views.getTopics),
    url(r'checkfollowuser/.*$', views.getButton),
    url(r'unfollowuser/.*$', views.unfollowuser),
    url(r'followuser/.*$', views.followuser),
    url(r'^post/.$', views.getAllPosts)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
