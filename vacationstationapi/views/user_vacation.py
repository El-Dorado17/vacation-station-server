"""View module for handling requests about user vacations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vacationstationapi.models import UserVacation, Vacation, VacationUser
from django.contrib.auth.models import User

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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = ('country', 'city', 'vacation_type', 'vacation_user',
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