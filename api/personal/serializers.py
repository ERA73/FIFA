from personal.models import *
from rest_framework import serializers


class EquipoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Equipo
		fields = ['id', 'nombre', 'imagen', 'escudo']


class JugadoresSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Jugadores
		fields = ['id', 'foto', 'nombre', 'apellido', 'fecha_nacimiento', 'posicion', 'numero', 'titular']


class JugadoresEquipoSerializer(serializers.HyperlinkedModelSerializer):
	equipo = EquipoSerializer(read_only=True, many=False)
	class Meta:
		model = Jugadores
		fields = ['equipo', 'foto', 'nombre', 'apellido', 'fecha_nacimiento', 'posicion', 'numero', 'titular']


class TecnicosSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tecnicos
		fields = ['id', 'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'rol']


class TecnicosEquipoSerializer(serializers.HyperlinkedModelSerializer):
	equipo = EquipoSerializer(read_only=True, many=False)
	class Meta:
		model = Tecnicos
		fields = ['equipo', 'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'rol']
