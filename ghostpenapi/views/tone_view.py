from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ghostpenapi.models import Tone
from ghostpenapi.serializers import ToneSerializer

class ToneView(ViewSet):
    def retrieve(self, pk):
        """Retrieve a specific tone by primary key."""
        try:
            tone = Tone.objects.get(pk=pk)
            serializer = ToneSerializer(tone)
            return Response(serializer.data)
        except Tone.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Retrieve a list of all contacts."""
        tones = Tone.objects.all()
        serializer = ToneSerializer(tones, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new contact."""
        serializer = ToneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Update an existing contact."""
        tone = Tone.objects.get(pk=pk)
        tone.label = request.data["label"]
        tone.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, pk):
        """Delete a contact."""
        tone = Tone.objects.get(pk=pk)
        tone.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)