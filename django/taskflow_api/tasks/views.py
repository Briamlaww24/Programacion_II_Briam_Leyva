from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """Vista de bienvenida de la app tasks."""
    return HttpResponse("Hola, Taskflow")

def exposicionbdd(request):
    """Vista de la exposición dobre base de datos"""
    return render(request, "index.html")