from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "patients/index.html")

# def patients(rqt):
#     return render(rqt, "patients/patients.html")