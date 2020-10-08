from rest_framework import serializers
from UserApp.models import Profiles

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = (
                    'Username',
                    'Bio',
                    'ProfileImage')
