from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Proprietor(models.Model):
    propiertor_name = models.CharField(max_length=100)
    def __str__(self):
        return self.propiertor_name

class Administrator(models.Model):
    administrator_name = models.CharField(max_length=100)    
    def __str__(self):
        return self.administrator_name

class Expense(models.Model):
    expense_name = models.CharField(max_length=50)
    expense_price = models.IntegerField()
    expense_paid = models.BooleanField()
    expense_emision_date = models.DateField(timezone.now)
    def __str__(self):
        return self.expense_name
    

class Site(models.Model):
    site_name = models.CharField(max_length=50)
    site_capacity = models.IntegerField()
    def __str__(self):
        return self.site_name