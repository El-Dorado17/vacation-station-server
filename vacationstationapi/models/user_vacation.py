from django.db import models
from django.contrib.auth.models import User

class UserVacation (models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vacation = models.ForeignKey("Vacation", on_delete=models.CASCADE)