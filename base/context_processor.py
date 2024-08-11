from .models import Service

def service_data(request):
    data = Service.objects.all()
    return {'service_data':data}
