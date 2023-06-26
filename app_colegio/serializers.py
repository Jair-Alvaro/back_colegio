from rest_framework import serializers
from .models import *

class ColegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblColegio
        fields = '__all__'

class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblZona
        fields = '__all__'

class EmpleadoHonorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpleadoHonorario
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblAlumno
        fields = '__all__'

class AlumnoHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblAlumnoHorario
        fields = '__all__'

class ApoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblApoderado
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblCargo
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblEmpleado
        fields = '__all__'

class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblFormaPago
        fields = '__all__'