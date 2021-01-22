from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Proprietor, Administrator, Expense, Site

# Create your views here.

class Index_view(TemplateView):
    template_name = 'inicio-sesion.html'
    def get(self, request):
        return render(request, self.template_name)

class Register_view(TemplateView):
    template_name = 'registro-usuario.html'
    def get(self, request):
        return render(request, self.template_name)

# Propiertor's views

class Link_neighborhood_view(TemplateView):
    template_name = 'vincular-vecindario.html'
    def get(self, request):
        return render(request, self.template_name)

class Propiertor_expense_view(ListView):
    model = Expense
    template_name = 'propietario-gastos.html'
    queryset = Expense.objects.order_by('expense_price')

class Propiertor_site_view(TemplateView):
    template_name = 'propietario-reservas.html'
    def get(self, request):
        return render(request, self.template_name)

# Administrator's views

class Administrator_register_neighborhood_view(TemplateView):
    template_name = 'registro-vecindario.html'
    def get(self, request):
        return render(request, self.template_name)

class Administrator_home_view(TemplateView):
    template_name = 'administrador-inicio.html'
    def get(self, request):
        return render(request, self.template_name)

class Administrator_list_view(TemplateView):
    template_name = 'administrador-lista.html'
    def get(self, request):
        return render(request, self.template_name)

class Administrator_expense_view(TemplateView):
    template_name = 'administrador-gastos.html'
    def get(self, request):
        return render(request, self.template_name)

class Administrator_site_view(TemplateView):
    template_name = 'administrador-reservas.html'
    def get(self, request):
        return render(request, self.template_name)

