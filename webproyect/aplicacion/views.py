from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Mi primera pagina Django!!!")

def viernes(request):
    return HttpResponse("Hoy es viernes")
