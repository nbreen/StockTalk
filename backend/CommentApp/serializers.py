from rest_framework import serializers
from CommentApp.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('CommentId',
        'Username',
        'PostId',
        'Comment',
        'CommentDate')
