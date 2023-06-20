from django.db import models
from django.contrib.auth.models import User


class UserVacation (models.Model):

    vacation_user = models.ForeignKey("VacationUser", on_delete=models.CASCADE, null = True)
    vacation = models.ForeignKey("Vacation", on_delete=models.CASCADE)