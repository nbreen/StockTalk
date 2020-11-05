from rest_framework import serializers
from PostApp.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('Username', 'PostId', 'UserId', 'TopicName', 'PostType', 'Post', 'PostDate', 'Downvotes', 'Upvotes', 'Anonymous', 'PostImage')
