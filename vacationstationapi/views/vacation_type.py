"""View module for handling requests about vacation types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vacationstationapi.models import VacationType

class VacationTypeView(ViewSet):
    """Vacation Station VacationType View"""

    def retrieve (self, request, pk):
        """handles GET requests for a single vacation type
        Returns:
            response -- JSON serialized vacation type
        """
        vacation_type = VacationType.objects.get(pk=pk)
        serializer = VacationTypeSerializer(vacation_type)
        return Response(serializer.data)
    
    def list (self,requeest):
        """
            GET requests for ALL vacation types
        """
        vacation_type = VacationType.objects.all()
        serializer = VacationTypeSerializer(vacation_type, many=True)
        return Response(serializer.data)

class VacationTypeSerializer(serializers.ModelSerializer):
    """
        JSON serializer for vacation types
    """
    class Meta:
        model  = VacationType
        fields = ('id', 'name')