from rest_framework import serializers
from ghostpenapi.models import Contact
from .ghostuser_serializer import GhostUserSerializer

class ContactSerializer(serializers.ModelSerializer):
    ghostuser = GhostUserSerializer(many=False)
    class Meta:
        model = Contact
        fields = ('id', 'ghostuser', 'first_name', 'last_name', 'bio')

class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields =('id', 'first_name', 'last_name', 'bio')