from rest_framework import serializers
from CommentApp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('Username',
                    'TopicName',
                    'UniqueIdentifier',
                    'TextField',
                    'Upvotes',
                    'Downvotes')
      