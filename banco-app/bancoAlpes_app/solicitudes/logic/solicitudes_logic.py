from ..models import Solicitud

def get_solicitudes():
    return Solicitud.objects.all()

def create_solicitud(form):
    solicitud = form.save
    solicitud.save()
    return ()
