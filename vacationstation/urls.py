from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]
# Requests to http://localhost:8000/register will be routed to the register_user function
# Requests to http://localhost:8000/login will be routed to the login_user function

#*To run the server
#* python3 manage.py runserver