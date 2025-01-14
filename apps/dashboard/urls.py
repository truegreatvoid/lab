from django.urls import path, include

from .views import *


app_name = 'dashboard'

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('frequencia/', Frequencia.as_view(), name='frequencia'),
]
