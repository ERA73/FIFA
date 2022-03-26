import traceback
import json
from itertools import tee
from django.db.models import Count
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response

# models
from personal.models import *

# serializers
from api.personal.serializers import *

# modules
from personal.functions import *

# VISTAS QUE RETORNAN LISTAS
class EquiposViewSet(generics.ListCreateAPIView):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Equipo.objects.all()
	serializer_class = EquipoSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]
	
	def post(self, request, *args, **kwargs):
		try:
			nombre = get_parameter('nombre', [request.data, kwargs], allow_empty=False).strip()
			imagen = get_parameter('imagen', [request.data, kwargs]).strip()
			escudo = get_parameter('escudo', [request.data, kwargs]).strip()

			data = {"nombre": nombre}
			if imagen:
				data["imagen"] = imagen
			if escudo:
				data["escudo"] = escudo
			equipo = Equipo(**data)
			equipo.save()
			serializer = EquipoSerializer([equipo], many=True)
			data = {'mensaje': "Creación de Equipo Exitosa",
					'code': 1, 'data': serializer.data[0]}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)


class JugadoresViewSet(generics.ListCreateAPIView):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Jugadores.objects.all()
	serializer_class = JugadoresSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]
	
	def post(self, request, *args, **kwargs):
		try:
			id_equipo = get_parameter('id_equipo', [request.data, kwargs], param_type=int, allow_empty=False)
			equipo = validate_model_list(Equipo.objects.filter(id=id_equipo), 'Equipo').first()

			nombre = get_parameter('nombre', [request.data, kwargs], allow_empty=False).strip()
			apellido = get_parameter('apellido', [request.data, kwargs], allow_empty=False).strip()
			fecha_nacimiento = get_parameter('fecha_nacimiento', [request.data, kwargs], allow_empty=False).strip()
			fecha_nacimiento = validate_type(['fecha', fecha_nacimiento], "Fecha de nacimiento Invalida")
			posicion = get_parameter('posicion', [request.data, kwargs], allow_empty=False).strip()
			numero = get_parameter('numero', [request.data, kwargs], param_type=int, allow_empty=False)
			if Jugadores.objects.filter(equipo=equipo, numero = numero).exists():
				raise Exception(f"Equipo [{equipo.nombre}] ya tiene un jugador con el numero [{numero}]")
			foto = get_parameter('foto', [request.data, kwargs]).strip()
			titular = get_parameter('titular', [request.data, kwargs], param_type=int)


			data = {
				"equipo": equipo,
				"nombre": nombre,
				"apellido": apellido,
				"fecha_nacimiento": fecha_nacimiento,
				"posicion": posicion,
				"numero": numero
			}
			if foto:
				data["foto"] = foto
			if titular:
				data["escudo"] = titular
			jugador = Jugadores(**data)
			jugador.save()
			serializer = JugadoresEquipoSerializer([jugador], many=True)
			data = {'mensaje': "Creación de Jugador Exitosa",
					'code': 1, 'data': serializer.data[0]}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)


class TecnicosViewSet(generics.ListCreateAPIView):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Tecnicos.objects.all()
	serializer_class = TecnicosSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]
	
	def post(self, request, *args, **kwargs):
		try:
			id_equipo = get_parameter('id_equipo', [request.data, kwargs], param_type=int, allow_empty=False)
			equipo = validate_model_list(Equipo.objects.filter(id=id_equipo), 'Equipo').first()

			nombre = get_parameter('nombre', [request.data, kwargs], allow_empty=False).strip()
			apellido = get_parameter('apellido', [request.data, kwargs], allow_empty=False).strip()
			fecha_nacimiento = get_parameter('fecha_nacimiento', [request.data, kwargs], allow_empty=False).strip()
			fecha_nacimiento = validate_type(['fecha', fecha_nacimiento], "Fecha de nacimiento Invalida")
			nacionalidad = get_parameter('nacionalidad', [request.data, kwargs], allow_empty=False).strip()
			rol = get_parameter('rol', [request.data, kwargs], allow_empty=False).strip()
			if rol not in ["técnico", "asistente", "médico", "preparador"]:
				raise Exception(f"El Rol [{rol}] es Invalido")

			data = {
				"equipo": equipo,
				"nombre": nombre,
				"apellido": apellido,
				"fecha_nacimiento": fecha_nacimiento,
				"nacionalidad": nacionalidad,
				"rol": rol
			}
			
			tecnico = Tecnicos(**data)
			tecnico.save()
			serializer = TecnicosEquipoSerializer([tecnico], many=True)
			data = {'mensaje': "Creación de Tecnico Exitosa",
					'code': 1, 'data': serializer.data[0]}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)


# VISTAS PARA CRUD

class EquipoViewSet(generics.RetrieveUpdateAPIView):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = Equipo.objects.all()
	serializer_class = EquipoSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]

	def get(self, request, *args, **kwargs):
		try:
			id_equipo = get_parameter('pk', [request.data, kwargs])
			queryset = validate_model_list(Equipo.objects.filter(id=id_equipo), 'Equipo')
			serializer = EquipoSerializer(queryset, many=True)
			data = {'mensaje': "Carga de Equipo Exitosa",
					'code': 1, 'data': serializer.data[0]}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)
	
	def put(self, request, *args, **kwargs):
		try:
			id_equipo = get_parameter('pk', [request.data, kwargs], param_type=int, allow_empty=False)
			nombre = get_parameter('nombre', [request.data, kwargs], allow_empty=False).strip()
			imagen = get_parameter('imagen', [request.data, kwargs]).strip()
			escudo = get_parameter('escudo', [request.data, kwargs]).strip()

			equipo = validate_model_list(Equipo.objects.filter(id=id_equipo), 'Equipo').first()
			data = {"nombre": nombre}
			if nombre:
				equipo.nombre = nombre
			if imagen:
				equipo.imagen = imagen
			if escudo:
				equipo.escudo = escudo
			
			equipo.save()
			serializer = EquipoSerializer([equipo], many=True)
			data = {'mensaje': "Actualización de Equipo Exitosa",
					'code': 1, 'data': serializer.data[0]}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)
	
	def delete(self, request, *args, **kwargs):
		try:
			id_equipo = get_parameter('pk', [request.data, kwargs], param_type=int, allow_empty=False)

			equipo = validate_model_list(Equipo.objects.filter(id=id_equipo), 'Equipo').first()
			
			equipo.delete()

			data = {'mensaje': "Equipo eliminado de forma Exitosa",
					'code': 1, 'data': None}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)

class JugadorViewSet(generics.RetrieveUpdateAPIView):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Jugadores.objects.all()
	serializer_class = JugadoresSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]

	def get(self, request, *args, **kwargs):
		try:
			id_jugador = get_parameter('pk', [request.data, kwargs])
			queryset = validate_model_list(Jugadores.objects.filter(id=id_jugador), 'Jugador')
			serializer = JugadoresSerializer(queryset, many=True)
			data = {'mensaje': "Carga de Jugador Exitosa",
					'code': 1, 'data': serializer.data[0]}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)
	
	def put(self, request, *args, **kwargs):
		try:
			id_jugador = get_parameter('pk', [request.data, kwargs], param_type=int, allow_empty=False)
			jugador = validate_model_list(Jugadores.objects.filter(id=id_jugador), 'Jugador').first()

			id_equipo = get_parameter('id_equipo', [request.data, kwargs])
			if id_equipo:
				id_equipo = get_parameter('id_equipo', [request.data, kwargs], param_type=int, allow_empty=False)
				equipo = validate_model_list(Equipo.objects.filter(id=id_equipo), 'Equipo').first()

			nombre = get_parameter('nombre', [request.data, kwargs]).strip()
			apellido = get_parameter('apellido', [request.data, kwargs]).strip()
			fecha_nacimiento = get_parameter('fecha_nacimiento', [request.data, kwargs]).strip()
			if fecha_nacimiento:
				fecha_nacimiento = validate_type(['fecha', fecha_nacimiento], "Fecha de nacimiento Invalida")
			posicion = get_parameter('posicion', [request.data, kwargs]).strip()
			numero = get_parameter('numero', [request.data, kwargs])
			if numero:
				numero = get_parameter('numero', [request.data, kwargs], param_type=int)
				if id_equipo:
					if Jugadores.objects.filter(equipo=equipo, numero = numero).exists():
						raise Exception(f"Equipo [{equipo.nombre}] ya tiene un jugador con el numero [{numero}]")
				else:
					if Jugadores.objects.filter(equipo=jugador.equipo, numero = numero).exists():
						raise Exception(f"Equipo [{jugador.equipo.nombre}] ya tiene un jugador con el numero [{numero}]")
			foto = get_parameter('foto', [request.data, kwargs]).strip()
			titular = get_parameter('titular', [request.data, kwargs])
			if titular:
				titular = get_parameter('titular', [request.data, kwargs], param_type=int)


			data = {}
			if equipo:
				jugador.equipo = equipo
			if nombre:
				jugador.nombre = nombre
			if apellido:
				jugador.apellido = apellido
			if fecha_nacimiento:
				jugador.fecha_nacimiento = fecha_nacimiento
			if posicion:
				jugador.posicion = posicion
			if numero:
				jugador.numero = numero
			if foto:
				jugador.foto = foto
			if titular:
				jugador.titular = titular
				
			jugador.save()
			serializer = JugadoresEquipoSerializer([jugador], many=True)
			data = {'mensaje': "Actualización de Jugador Exitosa",
					'code': 1, 'data': serializer.data[0]}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)
	
	def delete(self, request, *args, **kwargs):
		try:
			id_jugador = get_parameter('pk', [request.data, kwargs], param_type=int, allow_empty=False)

			jugador = validate_model_list(Jugadores.objects.filter(id=id_jugador), 'Jugador').first()
			
			jugador.delete()

			data = {'mensaje': "Jugador eliminado de forma Exitosa",
					'code': 1, 'data': None}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)


class TecnicoViewSet(generics.RetrieveUpdateAPIView):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Tecnicos.objects.all()
	serializer_class = TecnicosSerializer
	# permission_classes = [permissions.IsAuthenticated]
	permission_classes = [permissions.AllowAny]

	def get(self, request, *args, **kwargs):
		try:
			id_tecnico = get_parameter('pk', [request.data, kwargs])
			queryset = validate_model_list(Tecnicos.objects.filter(id=id_tecnico), 'Tecnico')
			serializer = TecnicosSerializer(queryset, many=True)
			data = {'mensaje': "Carga de Técnico  Exitosa",
					'code': 1, 'data': serializer.data[0]}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)
	
	def put(self, request, *args, **kwargs):
		try:
			id_tecnico = get_parameter('pk', [request.data, kwargs], param_type=int, allow_empty=False)
			tecnico = validate_model_list(Tecnicos.objects.filter(id=id_tecnico), 'Tecnico').first()

			id_equipo = get_parameter('id_equipo', [request.data, kwargs])
			if id_equipo:
				id_equipo = get_parameter('id_equipo', [request.data, kwargs], param_type=int, allow_empty=False)
				equipo = validate_model_list(Equipo.objects.filter(id=id_equipo), 'Equipo').first()

			nombre = get_parameter('nombre', [request.data, kwargs]).strip()
			apellido = get_parameter('apellido', [request.data, kwargs]).strip()
			fecha_nacimiento = get_parameter('fecha_nacimiento', [request.data, kwargs]).strip()
			if fecha_nacimiento:
				fecha_nacimiento = validate_type(['fecha', fecha_nacimiento], "Fecha de nacimiento Invalida")

			nacionalidad = get_parameter('nacionalidad', [request.data, kwargs]).strip()
			rol = get_parameter('rol', [request.data, kwargs]).strip()
			if rol:
				if rol not in ["técnico", "asistente", "médico", "preparador"]:
					raise Exception(f"El Rol [{rol}] es Invalido")

			data = {}
			if equipo:
				tecnico.equipo = equipo
			if nombre:
				tecnico.nombre = nombre
			if apellido:
				tecnico.apellido = apellido
			if fecha_nacimiento:
				tecnico.fecha_nacimiento = fecha_nacimiento
			if nacionalidad:
				tecnico.nacionalidad = nacionalidad
			if rol:
				tecnico.numero = rol
				
			tecnico.save()
			serializer = TecnicosEquipoSerializer([tecnico], many=True)
			data = {'mensaje': "Actualización de Tecnico Exitosa",
					'code': 1, 'data': serializer.data[0]}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)
	
	def delete(self, request, *args, **kwargs):
		try:
			id_tecnico = get_parameter('pk', [request.data, kwargs], param_type=int, allow_empty=False)

			tecnico = validate_model_list(Tecnicos.objects.filter(id=id_tecnico), 'Tecnico').first()
			
			tecnico.delete()

			data = {'mensaje': "Tecnico eliminado de forma Exitosa",
					'code': 1, 'data': None}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)


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
			
			data = {'mensaje': "Carga del Informe",
					'code': 1, 'data': resumen}
			return Response(data, status=201)
		except Exception as e:
			traceback.print_exc()
			data = {'message': e.args[0], 'code': 2, 'data': None}
			return Response(data, status=201)