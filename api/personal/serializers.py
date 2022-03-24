from personal.models import *
from rest_framework import serializers


class EquipoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Equipo
		fields = ['nombre', 'imagen', 'escudo']


class JugadoresSerializer(serializers.HyperlinkedModelSerializer):
	equipo = serializers.StringRelatedField(many=True)
	class Meta:
		model = Jugadores
		fields = ['equipo', 'foto', 'nombre', 'apellido', 'fecha_nacimiento', 'pocision', 'numero', 'titular']


class TecnicosSerializer(serializers.HyperlinkedModelSerializer):
	equipo = serializers.StringRelatedField(many=True)
	class Meta:
		model = Tecnicos
		fields = ['equipo', 'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'roll']
