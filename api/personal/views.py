import traceback
import json
from itertools import tee
from django.db.models import Count
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response

# models
from personal.models import *

# serializers
from api.personal.serializers import EquipoSerializer, JugadoresSerializer, TecnicosSerializer

# modules
from personal.functions import *


class EquipoViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Equipo.objects.all()
	serializer_class = EquipoSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]

	########################################################
	######################## FALTAN ########################
	# POST
	# PUT
	# DELETE
	########################################################


class JugadoresViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Jugadores.objects.all()
	serializer_class = JugadoresSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]

	########################################################
	######################## FALTAN ########################
	# POST
	# PUT
	# DELETE
	########################################################


class TecnicosViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Tecnicos.objects.all()
	serializer_class = TecnicosSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]

	########################################################
	######################## FALTAN ########################
	# POST
	# PUT
	# DELETE
	########################################################


class ReporteViewSet(generics.RetrieveUpdateAPIView):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Equipo.objects.all()
	serializer_class = EquipoSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]

	def get(self, request, *args, **kwargs):
		try:
			resumen = {}
			equipos_registrados = Equipo.objects.all().count()
			resumen["equipos_registrados"] = equipos_registrados

			total_jugadores = Jugadores.objects.all().count()
			resumen["total_jugadores"] = total_jugadores

			jugador_mas_joven = Jugadores.objects.all().order_by("-fecha_nacimiento").first().nombre
			resumen["jugador_mas_joven"] = jugador_mas_joven

			jugador_mas_viejo = Jugadores.objects.all().order_by("fecha_nacimiento").first().nombre
			resumen["jugador_mas_viejo"] = jugador_mas_viejo

			jugadores_suplentes = Jugadores.objects.filter(titular = 0).count()
			resumen["jugadores_suplentes"] = jugadores_suplentes

			promedio_suplentes_x_equipo = int(jugadores_suplentes/equipos_registrados)
			resumen["promedio_suplentes_x_equipo"] = promedio_suplentes_x_equipo

			equipo_mas_jugadores = Equipo.objects.annotate(num_comments=models.Count('equipo_jugador')).all().order_by("-num_comments").first()
			equipo_mas_jugadores = equipo_mas_jugadores.nombre
			resumen["equipo_mas_jugadores"] = equipo_mas_jugadores

			edad_promedio_jugadores = int(sum([calcular_edad(jugador.fecha_nacimiento) for jugador in Jugadores.objects.all()])/total_jugadores)
			resumen["edad_promedio_jugadores"] = edad_promedio_jugadores

			promedio_jugadores_equipo = int(total_jugadores/equipos_registrados)
			resumen["promedio_jugadores_equipo"] = promedio_jugadores_equipo

			tecnico_mas_viejo = Tecnicos.objects.filter(rol = "técnico").order_by("fecha_nacimiento").first().nombre
			resumen["tecnico_mas_viejo"] = tecnico_mas_viejo
			
			data = {'mensaje': "detalles de tarea",
					'code': 1, 'data': resumen}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)