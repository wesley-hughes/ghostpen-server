from rest_framework import serializers
from ghostpenapi.models import Campaign
from .contact_serializer import ContactSerializer
from .ghostuser_serializer import GhostUserSerializer

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        contacts = ContactSerializer(many=True)
        ghostuser = GhostUserSerializer(many=False)
        model = Campaign
        fields = ('id', 'label', 'description', 'contacts', 'ghostuser')

class CreateCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'label', 'description', 'ghostuser')