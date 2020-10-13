from rest_framework import serializers
from ProfileApp.models import Profiles

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = (
                    'Username',
                    'Bio',
                    'ProfileImage')
