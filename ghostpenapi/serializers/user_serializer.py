from rest_framework import serializers
from django.contrib.auth.models import User
from ghostpenapi.serializers import GhostUserSerializer

class UserSerializer(serializers.ModelSerializer):
    ghostuser = GhostUserSerializer()
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'ghostuser')
