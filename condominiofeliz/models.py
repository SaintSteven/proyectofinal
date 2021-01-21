from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Proprietor(models.Model):
    propiertor_name = models.CharField(max_length=100)

class Administrator(models.Model):
    administrator_name = models.CharField(max_length=100)    

class Expense(models.Model):
    expense_name = models.CharField(max_length=50)
    expense_price = models.IntegerField

class Site(models.Model):
    site_name = models.CharField(max_length=50)
    site_capacity = models.IntegerField