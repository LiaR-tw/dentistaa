from django.contrib import admin

# Register your models here.

from .models import patients

admin.site.register(patients)