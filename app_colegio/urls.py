from rest_framework.routers import DefaultRouter
from django.urls import path,include

from . import views

route = DefaultRouter()

route.register(r'colegio', views.ColegioDetailView,basename= 'colegio')
route.register(r'zona', views.ZonaDetailView, basename='zona')
route.register(r'empleadohonorario', views.EmpleadoHonorarioDetailView, basename='empleadohonorario')
route.register(r'alumno', views.AlumnoDetailView, basename='alumno')
route.register(r'alumnohorario', views.AlumnoHorarioDetailView, basename='alumnohorario')
route.register(r'apoderado', views.ApoderadoDetailView, basename='apoderado')
route.register(r'cargo', views.CargoDetailView, basename='cargo')
route.register(r'empleado', views.EmpleadoDetailView, basename='empleado')
route.register(r'formapago', views.FormaPagoDetailView, basename='formapago')

urlpatterns = [
        path('api/', include(route.urls))
]