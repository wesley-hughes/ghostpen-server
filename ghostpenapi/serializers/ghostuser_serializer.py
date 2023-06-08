from rest_framework import serializers
from django.contrib.auth.models import User
from ghostpenapi.models import GhostUser

class GhostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhostUser
        fields = ('id', 'first_name', 'last_name', 'bio')
        depth = 1