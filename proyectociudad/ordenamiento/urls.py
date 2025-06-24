from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta principal para el listado
    path('crear_parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('crear_barrio/', views.crear_barrio, name='crear_barrio'),
]