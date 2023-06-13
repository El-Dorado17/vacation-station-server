from django.db import models

class VacationType (models.Model):

    name = models.CharField(max_length=80)