from django.db import models
from django.utils import timezone 


# Create your models here.

class patients(models.Model): 
    name = models.CharField(max_length=100)

    date = models.DateField()
    def createdat(self):
        return self.pub_date >= timezone.now()
    nextdate = models.DateField()
    def __str__(self):
        return self.name

