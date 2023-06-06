from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ghostpenapi.models import Contact, GhostUser
from ghostpenapi.serializers import ContactSerializer, CreateContactSerializer

class ContactView(ViewSet):
    """View set for managing contact information."""

    def retrieve(self, pk):
        """Retrieve a specific contact by primary key."""
        try:
            contact = Contact.objects.get(pk=pk)
            serializer = ContactSerializer(contact)
            return Response(serializer.data)
        except Contact.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Retrieve a list of all contacts."""
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new contact."""
        ghostuser = GhostUser.objects.get(user=request.auth.user)
        serializer = CreateContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(ghostuser=ghostuser)
        return Response(serializer.data, status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Update an existing contact."""
        contact = Contact.objects.get(pk=pk)
        contact.first_name = request.data["first_name"]
        contact.last_name = request.data["last_name"]
        contact.bio = request.data["bio"]
        contact.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, pk):
        """Delete a contact."""
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
