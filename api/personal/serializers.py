from personal.models import *
from rest_framework import serializers


class EquipoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Equipo
		fields = ['nombre', 'imagen', 'escudo']


class JugadoresSerializer(serializers.HyperlinkedModelSerializer):
	# equipo = EquipoSerializer(read_only=True, many=False)
	class Meta:
		model = Jugadores
		# fields = ['equipo', 'foto', 'nombre', 'apellido', 'fecha_nacimiento', 'posicion', 'numero', 'titular']
		fields = ['foto', 'nombre', 'apellido', 'fecha_nacimiento', 'posicion', 'numero', 'titular']


class TecnicosSerializer(serializers.HyperlinkedModelSerializer):
	# equipo = EquipoSerializer(read_only=True, many=False)
	class Meta:
		model = Tecnicos
		# fields = ['equipo', 'nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'rol']
		fields = ['nombre', 'apellido', 'fecha_nacimiento', 'nacionalidad', 'rol']
