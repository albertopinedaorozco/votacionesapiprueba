from rest_framework import serializers
from .models import Votante


class VotanteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nombres','apellidos','direccion','num_cedula','barrio','puesto_votacion','mesa')
        model = Votante

    def create(self, validated_data):
        validated_data['lider'] = self.context['request'].user
        return super(VotanteSerializer, self).create(validated_data)