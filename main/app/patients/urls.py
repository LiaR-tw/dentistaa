from . import views
from django.urls import path 
urlpatterns = [

    path('', views.index, name="index.html"),
    # path('patients/', views.patients, name="patients"),
    # path('services/', views.services, name="services"),
]
    