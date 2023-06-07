from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ghostpenapi.models import Letter
from ghostpenapi.serializers import LetterSerializer

class LetterView(ViewSet):
    def retrieve(self, request, pk):
        """Retrieve a specific letter by primary key."""
        try:
            letter = Letter.objects.get(pk=pk)
            serializer = LetterSerializer(letter)
            return Response(serializer.data)
        except Letter.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Retrieve a list of all letters."""
        letters = Letter.objects.all()
        serializer = LetterSerializer(letters, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new letter."""
        serializer = LetterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(contact=request.data['contact']) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update an existing letter."""
        letter = Letter.objects.get(pk=pk)
        serializer = LetterSerializer(letter, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(contact=request.data['contact'])
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, pk):
        """Delete a letter."""
        letter = Letter.objects.get(pk=pk)
        letter.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
