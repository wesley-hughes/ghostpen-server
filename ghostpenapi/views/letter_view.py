from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from ghostpenapi.models import Letter, Contact, GhostUser, Campaign
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
        ghostuser = GhostUser.objects.get(user=request.auth.user)
        contact_filter = request.query_params.get('contact', None)
        campaign = request.query_params.get('campaign', None)

        filters = {}
        if contact_filter is not None:
            filters['contact__first_name__icontains']= contact_filter
        if campaign is not None:
            filters['campaign']= campaign

        try:
            letters = Letter.objects.filter(Q(**filters), ghostuser=ghostuser)
            serializer = LetterSerializer(letters, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Letter.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def create(self, request):
        """Create a new letter."""
        serializer = CreateLetterSerializer(data=request.data)
        contact= Contact.objects.get(pk=request.data['contact'])
        ghostuser= GhostUser.objects.get(user=request.auth.user)
        
        campaign= None
        if 'campaign' in request.data:
            campaign = Campaign.objects.get(pk=request.data["campaign"])
        
        serializer.is_valid(raise_exception=True)
        serializer.save(contact=contact, ghostuser=ghostuser, campaign=campaign)
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
