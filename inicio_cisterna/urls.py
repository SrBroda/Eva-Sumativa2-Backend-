from django.urls import path

from . import views

app_name = 'inicio_cisterna'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tema/<slug:slug>/', views.tema_detalle, name='tema_detalle'),
]
