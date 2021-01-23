from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index_view.as_view(), name="inicio-sesion"),
    path('inicio-sesion', views.Index_view.as_view(), name="inicio-sesion"),
    path('registro-usuario', views.Register_view.as_view(), name="registro-usuario"),

    path('propietario/vincular-vecindario', views.Link_neighborhood_view.as_view(), name="vincular-vecindario"),
    path('propietario/gastos', views.Propiertor_expense_view.as_view(), name="propietario-gastos"),
    path('propietario/reservas', views.Propiertor_site_view.as_view(), name="propietario-reservas"),

    path('administrador/registrar-vecindario', views.Administrator_register_neighborhood_view.as_view(), name="registrar-vecindario"),
    path('administrador/inicio', views.Administrator_home_view.as_view(), name="administrador-inicio"),
    path('administrador/lista', views.Administrator_list_view.as_view(), name="administrador-lista"),
    path('administrador/gastos', views.Administrator_expense_view.as_view(), name="administrador-gastos"),
    path('administrador/reservas', views.Administrator_site_view.as_view(), name="administrador-reservas"),

    path('holachao', views.Hola.as_view()),
]