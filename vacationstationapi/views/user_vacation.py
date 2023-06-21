"""View module for handling requests about user vacations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vacationstationapi.models import UserVacation, Vacation, VacationUser
from django.contrib.auth.models import User
from vacationstationapi.models import VacationType
from vacationstationapi.models import Country


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
    
    def list (self,request):
        """
            GET requests for ALL user vacations
        """
        vacation_user= VacationUser.objects.get(user = request.auth.user)
        user_vacations = UserVacation.objects.filter(vacation_user = vacation_user)
        serializer = UserVacationSerializer(user_vacations, many=True)
        return Response(serializer.data)
    
    # def update(self, request, pk):
    #     """Handle PUT requests for a vacation
    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """
    #     user_vacation = UserVacation.objects.get(pk=pk)
    #     country = Country.objects.get(pk=request.data["country"])
    #     user_vacation.country = country
    #     user_vacation.city = request.data["city"]
    #     vacation_type = VacationType.objects.get(pk=request.data["vacation_type"])
    #     user_vacation.vacation_type = vacation_type
    #     # vacation_user = VacationUser.objects.get(pk=request.data["vacation_user"])
    #     # vacation.vacation_user = vacation_user
    #     user_vacation.description = request.data["description"]
    #     user_vacation.number_of_people = request.data["number_of_people"]
    #     user_vacation.price = request.data["price"]
    #     user_vacation.rating = request.data["rating"]
        
    #     user_vacation.save()

    # def destroy(self, request, pk):
    #     user_vacation = UserVacation.objects.get(pk=pk)
    #     user_vacation.delete()
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ('id', 'country', 'city', 'vacation_type', 'vacation_user',
                'description', 'number_of_people', 'price', 'rating')
        depth = 1

    

class UserVacationSerializer(serializers.ModelSerializer):
    """
        JSON serializer for Countries
    """
    #user =UserSerializer()
    vacation = VacationSerializer()
    # vacation = 
    class Meta:
        model  = UserVacation
        fields = ('id', 'vacation_user', 'vacation')