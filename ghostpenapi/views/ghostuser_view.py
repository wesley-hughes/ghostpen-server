from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from ghostpenapi.models import GhostUser
from ghostpenapi.serializers import GhostUserSerializer

class GhostUserView(ViewSet):
    def retrieve(self, pk):
        """Retrieve a specific tone by primary key."""
        try:
            ghostuser = GhostUser.objects.get(pk=pk)
            serializer = GhostUserSerializer(ghostuser)
            return Response(serializer.data)
        except GhostUser.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        