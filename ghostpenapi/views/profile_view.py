from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from ghostpenapi.serializers import UserSerializer

class ProfileView(ViewSet):
    @action(methods=['GET'], detail=False, url_path="my-profile")
    def my_profile(self, request):
        """Get the current user's profile"""
        try:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['PUT'], detail=False)
    def edit(self, request):
        """Edit the current user's profile"""
        user = request.auth.user
        user.username = request.data['username']
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.bio = request.data['bio']
        if request.data.get('password', None):
            user.set_password(request.data['password'])
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)