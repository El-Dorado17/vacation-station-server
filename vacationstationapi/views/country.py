"""View module for handling requests about countries"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vacationstationapi.models import Country

class CountryView(ViewSet):
    """Vacation Station Countries View"""

    def retrieve (self, request, pk):
        """handles GET requests for a single country
        Returns:
            response -- JSON serialized country
        """
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country)
        return Response(serializer.data)
    
    def list (self,request):
        """
            GET requests for ALL countries
        """
        country = Country.objects.all()
        serializer = CountrySerializer(country, many=True)
        return Response(serializer.data)

class CountrySerializer(serializers.ModelSerializer):
    """
        JSON serializer for Countries
    """
    class Meta:
        model  = Country
        fields = ('id', 'name')