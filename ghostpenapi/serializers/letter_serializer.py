from rest_framework import serializers, status

class LetterSerializer(serializers.ModelSerializer):
    user = 