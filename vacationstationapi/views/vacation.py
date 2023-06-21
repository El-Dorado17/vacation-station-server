"""View module for handling requests about vacations"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from vacationstationapi.models import Vacation, VacationType
from vacationstationapi.models import Country, VacationUser, UserVacation
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


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
        #user = User.objects.get(user = request.auth.user)
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
        # vacation_id = vacation.id
        user_vacation = UserVacation.objects.create(vacation_user = vacation_user, vacation = vacation)
        serializer = VacationSerializer(vacation) 
        return Response(serializer.data, status= status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a vacation
        Returns:
            Response -- Empty body with 204 status code
        """
        vacation = Vacation.objects.get(pk=pk)
        country = Country.objects.get(pk=request.data["country"])
        vacation.country = country
        vacation.city = request.data["city"]
        vacation_type = VacationType.objects.get(pk=request.data["vacation_type"])
        vacation.vacation_type = vacation_type
        # vacation_user = VacationUser.objects.get(pk=request.data["vacation_user"])
        # vacation.vacation_user = vacation_user
        vacation.description = request.data["description"]
        vacation.number_of_people = request.data["number_of_people"]
        vacation.price = request.data["price"]
        vacation.rating = request.data["rating"]
        
        vacation.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            vacation = Vacation.objects.get(id=pk)
            vacation.delete()
            return Response( status=status.HTTP_204_NO_CONTENT)
        except Vacation.DoesNotExist:
            return Response("Vacation not found", status=status.HTTP_404_NOT_FOUND)


class VacationSerializer(serializers.ModelSerializer):
    """
        JSON serializer for vacation 
    """
    class Meta:
        model  = Vacation
        fields = ('id', 'country', 'city', 'vacation_type',
                    'vacation_user', 'description', 'number_of_people', 'price', 'rating')
