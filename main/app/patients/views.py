from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "patients/index.html")

def contact(request):
    return render(request, "patients/contacto.html")

def servicios(request):
    return render(request, "patients/servicios.html")

