from rest_framework import serializers
from TopicApp.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('TopicName',
                    'IsStock')
