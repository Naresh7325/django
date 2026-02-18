from django.db import models

# Create your models here.
class Service(models.Model):
    serviceName=models.CharField(max_length=100)
    serviceType = models.CharField(max_length=100)
    serviceDate = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
