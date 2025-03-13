from django.shortcuts import render
from hospitales.models import ServiceDepartamentos
from hospitales.models import ServiceHospitales

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def departamentosBBDD(request):
    servicio = ServiceDepartamentos()
    departamentos = servicio.getDepartamentos()
    context = {
        "departamentos": departamentos
    }
    return render(request, 'pages/departamentos.html', context)

def hospitalesBBDD(request):
    servicio = ServiceHospitales()
    hospital = servicio.getHospitales()
    context = {
        "hospitales": hospital
    }
    return render(request, 'pages/hospitales.html', context)

