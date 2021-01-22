from django.contrib import admin
from .models import Administrator, Proprietor, Expense, Site
# Register your models here.

admin.site.register(Administrator)
admin.site.register(Proprietor)
admin.site.register(Expense)
admin.site.register(Site)