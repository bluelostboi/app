from operator import mod
from typing_extensions import Required
from django.db import models

# Create your models here.
class Inventory(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=280)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    mfg_date = models.DateField()
    exp_date = models.DateField()