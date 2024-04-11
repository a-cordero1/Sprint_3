from django import forms

from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class meta: 
        model= Solicitud
        fields=[
            'id',
            'tipo',
            'fecha',
        ]
        labels= {
            'id':'Id',
            'tipo':'Tipo',
            'fecha':'Fecha',
        }
