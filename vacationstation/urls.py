from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from vacationstationapi.views import register_user, login_user
from rest_framework import routers
from vacationstationapi.views import CountryView, UserVacationView
from vacationstationapi.views import VacationUserView
from vacationstationapi.views import VacationTypeView, VacationView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'countries', CountryView, 'country')
router.register(r'uservacations', UserVacationView, 'uservacation')
router.register(r'users', VacationUserView, 'user') 
router.register(r'vacationtypes', VacationTypeView, 'vacationtype')
router.register(r'vacations', VacationView, 'vacation')


urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)), #This lets the router variable work if it needs to be country or any other resource
]
# Requests to http://localhost:8000/register will be routed to the register_user function
# Requests to http://localhost:8000/login will be routed to the login_user function

#*To run the server
#* python3 manage.py runserver
