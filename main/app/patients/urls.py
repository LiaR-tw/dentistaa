from . import views
from django.urls import path 
urlpatterns = [

    path('', views.index, name="index.html"),
    path('contacto/', views.contact, name="contact"),
    path('servicios/', views.servicios, name="servicios"),
]
    