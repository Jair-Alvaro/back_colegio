from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from .models import * 
from .serializers import * 


class ColegioDetailView(viewsets.ModelViewSet):
    queryset = TblColegio.objects.all()
    serializer_class = ColegioSerializer

class ZonaDetailView(viewsets.ModelViewSet):
    queryset = TblZona.objects.all()
    serializer_class = ZonaSerializer

class EmpleadoHonorarioDetailView(viewsets.ModelViewSet):
    queryset = EmpleadoHonorario.objects.all()
    serializer_class = EmpleadoHonorarioSerializer

class AlumnoDetailView(viewsets.ModelViewSet):
    queryset = TblAlumno.objects.all()
    serializer_class = AlumnoSerializer

class AlumnoHorarioDetailView(viewsets.ModelViewSet):
    queryset = TblAlumnoHorario.objects.all()
    serializer_class = AlumnoHorarioSerializer

class ApoderadoDetailView(viewsets.ModelViewSet):
    queryset = TblApoderado.objects.all()
    serializer_class = ApoderadoSerializer

class CargoDetailView(viewsets.ModelViewSet):
    queryset = TblCargo.objects.all()
    serializer_class = CargoSerializer

class EmpleadoDetailView(viewsets.ModelViewSet):
    queryset = TblEmpleado.objects.all()
    serializer_class = EmpleadoSerializer

class FormaPagoDetailView(viewsets.ModelViewSet):
    queryset = TblFormaPago.objects.all()
    serializer_class = FormaPagoSerializer