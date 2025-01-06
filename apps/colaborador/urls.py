from django.urls import path, include

from .views import *


app_name = 'colaborador'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]
