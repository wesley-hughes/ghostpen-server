from rest_framework import serializers
from ghostpenapi.models import Letter, Contact
from .contact_serializer import ContactSerializer

class LetterSerializer(serializers.ModelSerializer):
    contact = ContactSerializer() 
    class Meta:
        model = Letter
        fields = ('id', 'contact', 'ghostuser', 'letter_body', 'date')
        depth = 1

class CreateLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ('id', 'contact', 'ghostuser', 'letter_body', 'date')
