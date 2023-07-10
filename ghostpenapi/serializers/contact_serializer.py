from rest_framework import serializers
from ghostpenapi.models import Contact
from .tag_serializer import TagSerializer

class ContactSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Contact
        fields = ('id', 'ghostuser', 'first_name', 'last_name', 'tags', 'bio', 'name')
        depth = 1
class CreateContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'tags', 'bio')


