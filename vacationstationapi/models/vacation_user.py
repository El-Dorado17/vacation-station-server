from django.db import models
from django.contrib.auth.models import User

class VacationUser (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

#    ImportError: cannot import name 'User' from 'vacationstationapi.models'
# (/home/useradd/workspace/vacation-station-server/vacationstationapi/models/__init__.py)