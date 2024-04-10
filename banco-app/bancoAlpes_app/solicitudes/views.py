from django.shortcuts import render
from .logic.solicitudes_logic import get_solicitudes ,create_solicitud

def solicitud_list(request):
    solicitudes = get_solicitudes()
    context={'solicitudesList':solicitudes}
    return render(request, '<ruta_html>',context)

def solicitud_create(request):
    if request.method == 'POST':
        form = VariableForm(request.POST)
        if form.is_valid():
            create_variable(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created variable')
            return HttpResponseRedirect(reverse('variableCreate'))
        else:
            print(form.errors)
    else:
        form = VariableForm()

    context = {
        'form': form,
    }
    return render(request, 'Variable/variableCreate.html', context)

# Create your views here.
