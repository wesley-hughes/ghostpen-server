from rest_framework import serializers
from ghostpenapi.models import Tone

class ToneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tone
        fields = ('id', 'label')

