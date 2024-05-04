from django.db import models
from django.db.models import Model

# Create your models here.

class StockData(models.Model):
    tickersymbol = models.CharField(max_length=10)
    date = models.DateField()
    openprice = models.DecimalField(max_digits=6, decimal_places=2)
    closeprice = models.DecimalField(max_digits=6, decimal_places=2)