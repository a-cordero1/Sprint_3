from django.shortcuts import render
from .logic.solicitudes_logic import get_solicitudes ,create_solicitud
from .forms import SolicitudForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse



def solicitud_list(request):
    solicitudes = get_solicitudes()
    context={'solicitudesList':solicitudes}
    return render(request, 'solicitudes/solicitudes.html',context)

def solicitud_create(request):
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud_create(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created variable')
            return HttpResponseRedirect(reverse('variableCreate'))
        else:
            print(form.errors)
    else:
        form = SolicitudForm()

    context = {
        'form': form,
    }
    return render(request, 'solicitudes/create_solicitud.html', context)

    
# Create your views here.
