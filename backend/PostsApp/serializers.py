from rest_framework import serializers
from PostsApp.models import Posts

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('PostId',
        'Username',
        'TopicName',
        'PostType',
        'Post',
        'PostDate',
        'Downvotes',
        'Upvotes',
        'Anonymous',
        'PostImage')
