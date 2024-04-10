from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('solicitudes/', views.solicitud_list, name='solicitudesList'),
    #path('variablecreate/', csrf_exempt(views.variable_create), name='variableCreate'),
]