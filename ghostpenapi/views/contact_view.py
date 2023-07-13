from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ghostpenapi.models import Contact, GhostUser, Tag
from ghostpenapi.serializers import ContactSerializer, CreateContactSerializer

class ContactView(ViewSet):
    """View set for managing contact information."""

    def retrieve(self, request, pk=None):
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
        ghostuser = GhostUser.objects.get(user=request.auth.user)

        if ghostuser is not None:
            contacts = contacts.filter(ghostuser__user=request.auth.user)

        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Create a new contact."""
        ghostuser = GhostUser.objects.get(user=request.auth.user)
        all_tags = []
        tags = request.data["tags"]
        for tag in tags:
            contact_tag = Tag.objects.get(pk=tag)
            all_tags.append(contact_tag)
        serializer = CreateContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(ghostuser=ghostuser, tags=all_tags)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Update an existing contact."""
        contact = Contact.objects.get(pk=pk)
        contact.ghostuser = GhostUser.objects.get(user=request.auth.user)
        contact.bio = request.data["bio"]
        contact.first_name = request.data["first_name"]
        contact.last_name = request.data["last_name"]
        all_tags = []
        tags = request.data["tags"]
        for tag in tags:
            contact_tag = Tag.objects.get(pk=tag)
            all_tags.append(contact_tag)
        contact.tags.set(all_tags)
        contact.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """Delete a contact."""
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
