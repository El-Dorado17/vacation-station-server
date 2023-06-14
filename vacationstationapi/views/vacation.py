"""View module for handling requests about vacations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vacationstationapi.models import Vacation

class VacationView(ViewSet):
    """Vacation Station Vacation View"""

    def retrieve (self, request, pk):
        """handles GET requests for a single vacation 
        Returns:
            response -- JSON serialized vacation 
        """
        vacation = Vacation.objects.get(pk=pk)
        serializer = VacationSerializer(vacation)
        return Response(serializer.data)
    
    def list (self,requeest):
        """
            GET requests for ALL vacation 
        """
        vacation = Vacation.objects.all()
        serializer = VacationSerializer(vacation, many=True)
        return Response(serializer.data)

class VacationSerializer(serializers.ModelSerializer):
    """
        JSON serializer for vacation 
    """
    class Meta:
        model  = Vacation
        fields = ('id', 'country', 'city', 'vacation_type',
                    'user', 'description', 'number_of_people', 'price', 'rating')