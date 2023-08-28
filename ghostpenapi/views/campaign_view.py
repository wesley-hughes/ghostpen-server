from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ghostpenapi.models import Campaign, Contact, GhostUser
from ghostpenapi.serializers import CampaignSerializer
from rest_framework.decorators import action


class CampaignView(ViewSet):
    def retrieve(self, request, pk):
        """Retrieve a specific campaign by primary key."""
        try:
            campaign = Campaign.objects.get(pk=pk)
            serializer = CampaignSerializer(campaign)
            return Response(serializer.data)
        except Campaign.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        """Retrieve a list of all campaigns."""
        campaigns = Campaign.objects.all()
        ghostuser = GhostUser.objects.get(user=request.auth.user)
        if ghostuser is not None:
            campaigns = campaigns.filter(ghostuser__user=request.auth.user)
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Create a new campaign."""
        ghost_user = GhostUser.objects.get(user=request.auth.user)
        new_campaign = Campaign.objects.create(ghostuser=ghost_user, label=request.data["label"], description=request.data["description"])
        serializer = CampaignSerializer(new_campaign)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        """Update an existing campaign."""
        ghost_user = GhostUser.objects.get(user=request.auth.user)
        campaign = Campaign.objects.get(pk=pk)
        campaign.ghostuser=ghost_user
        campaign.label= request.data["label"]
        campaign.description= request.data["description"]
        campaign.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)  
      
    def destroy(self, request, pk):
        """Delete a campaign."""
        campaign = Campaign.objects.get(pk=pk)
        campaign.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def target(self, request, pk):
        '''add conacts to campaign'''
        campaign = Campaign.objects.get(pk=pk)
        contacts = request.data["contacts"]
        for contact in contacts:
            campaign.contacts.add(contact)
        return Response({'message': 'Contacts added'}, status=status.HTTP_201_CREATED)