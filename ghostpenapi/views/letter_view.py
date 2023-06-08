from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ghostpenapi.models import Letter, Contact, GhostUser
from ghostpenapi.serializers import LetterSerializer, CreateLetterSerializer

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
        serializer = CreateLetterSerializer(data=request.data)
        contact= Contact.objects.get(pk=request.data['contact'])
        ghostuser = GhostUser.objects.get(user=request.auth.user)
        serializer.is_valid(raise_exception=True)
        serializer.save(contact=contact, ghostuser=ghostuser) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Update an existing letter."""
        letter = Letter.objects.get(pk=pk)
        letter.ghostuser = GhostUser.objects.get(user=request.auth.user.id)
        letter.letter_body = request.data["letter_body"]
        contact_id = request.data["contact"]["id"]
        contact = Contact.objects.get(pk=contact_id) 
        letter.contact = contact 
        letter.date = request.data["date"]
        letter.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """Delete a letter."""
        letter = Letter.objects.get(pk=pk)
        letter.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
