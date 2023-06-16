"""View module for handling requests about vacations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vacationstationapi.models import Vacation, VacationType
from vacationstationapi.models import Country, VacationUser
from django.contrib.auth.models import User


class VacationView(ViewSet):
    """Vacation Station Vacation View"""

    def retrieve (self, request, pk):
        """handles GET requests for a single vacation 
        Returns:
            response -- JSON serialized vacation 
        """
        vacation = Vacation.objects.get(pk=pk)
        #vacation_user = VacationUser.objects.get(user= request.auth.user)
        serializer = VacationSerializer(vacation)
        return Response(serializer.data)
    
    def list (self,request):
        """
            GET requests for ALL vacation 
        """
        vacation = Vacation.objects.all()
        serializer = VacationSerializer(vacation, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        vacation_user = VacationUser.objects.get(user=request.auth.user)
        vacation_type = VacationType.objects.get(pk=request.data["vacation_type"])
        country = Country.objects.get(pk=request.data["country"])
# This is an outside model that gets used on line 47
        vacation = Vacation.objects.create(
            country=country,
            city=request.data["city"],
            vacation_type=vacation_type,
            vacation_user=vacation_user,
            description=request.data["description"],
            number_of_people=request.data["number_of_people"],
            price=request.data["price"],
            rating=request.data["rating"]
        )
        serializer = VacationSerializer(vacation) #Front end needs this in JSON: Whole point of serializing
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    

    def destroy(self, request, pk):
        vacation = Vacation.objects.get(pk=pk)
        vacation.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class VacationSerializer(serializers.ModelSerializer):
    """
        JSON serializer for vacation 
    """
    class Meta:
        model  = Vacation
        fields = ('id', 'country', 'city', 'vacation_type',
                    'vacation_user', 'description', 'number_of_people', 'price', 'rating')