"""View module for handling requests about Users"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vacationstationapi.models import VacationUser




class VacationUserView(ViewSet):
    """Vacation Station User View"""

    def retrieve (self, request, pk):
        """handles GET requests for a single user
        Returns:
            response -- JSON serialized user
        """
        vacation_user = VacationUser.objects.get(pk=pk)
        serializer = UserSerializer(vacation_user)
        return Response(serializer.data)
    
    def list (self,requeest):
        """
            GET requests for ALL users
        """
        vacation_user = VacationUser.objects.all()
        serializer = UserSerializer(vacation_user, many=True)
        return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    """
        JSON serializer for VacationUsers
    """
    class Meta:
        model  = VacationUser
        fields = ('id', 'user') #deleted bio field - not needed


        #!OperationalError: no such table: vacationstationapi_user