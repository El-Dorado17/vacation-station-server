from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Vacation (models.Model):

    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    city = models.CharField(max_length=80)
    vacation_type = models.ForeignKey("VacationType", on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=9000)
    number_of_people = models.IntegerField()
    price = models.FloatField()
    rating = models.IntegerField()
