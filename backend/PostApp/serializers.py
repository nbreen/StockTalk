from rest_framework import serializers
from PostApp.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('PostID',
                    'Username',
                    'Text',
                    'Image',
                    'Topic',
                    'Upvotes',
                    'Downvotes')
