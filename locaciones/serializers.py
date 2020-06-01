from rest_framework import serializers
from .models import Departamento,Municipio,PuestoVotacion


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nombre')
        model = Departamento

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nombre', 'departamento')
        model = Municipio

class PuestoVotacionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nombre', 'direccion','municipio')
        model = PuestoVotacion