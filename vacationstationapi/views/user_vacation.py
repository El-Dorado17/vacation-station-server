"""View module for handling requests about user vacations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vacationstationapi.models import UserVacation

class UserVacationView(ViewSet):
    """Vacation Station UserVacation View"""

    def retrieve (self, request, pk):
        """handles GET requests for a single country
        Returns:
            response -- JSON serialized country
        """
        user_vacation = UserVacation.objects.get(pk=pk)
        serializer = UserVacationSerializer(user_vacation)
        return Response(serializer.data)
    
    def list (self,requeest):
        """
            GET requests for ALL user vacations
        """
        user_vacation = UserVacation.objects.all()
        serializer = UserVacationSerializer(user_vacation, many=True)
        return Response(serializer.data)

class UserVacationSerializer(serializers.ModelSerializer):
    """
        JSON serializer for Countries
    """
    class Meta:
        model  = UserVacation
        fields = ('id', 'user', 'vacation')