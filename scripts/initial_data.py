from datetime import date
from personal.models import *

num_jugadores = 0
num_tecnicos = 0

def generar_jugadores(anno, grupo):
	global num_jugadores
	jugadores = []
	count = 1
	for tipos in grupo:
		mes = 0
		posicion, cantidad = tipos
		for index in range(1,cantidad+1):
			jugadores.append({
				"nombre": f"nombre_{num_jugadores}", 
				"apellido": f"apellido_{num_jugadores}", 
				"fecha_nacimiento": date(anno,1+(mes%12),1), 
				"posicion": posicion, 
				"numero": count, 
				"titular": index%2
				})
			count += 1
			num_jugadores += 1
			mes += 1
		anno += 1
	return jugadores

def generar_tecnicos(anno, grupo):
	global num_tecnicos
	tecnicos = []
	nacionalidad = ["pais_1","pais_2","pais_3","pais_4"]
	count = 1
	for tipos in grupo:
		mes = 0
		rol, cantidad = tipos
		for index in range(1,cantidad+1):
			tecnicos.append({
				"nombre": f"{rol}_{num_tecnicos}", 
				"apellido": f"apellido_{num_tecnicos}", 
				"fecha_nacimiento": date(anno,1+(mes%12),1), 
				"nacionalidad": nacionalidad[len(tecnicos)%len(nacionalidad)], 
				"rol": rol
				})
			count += 1
			num_tecnicos += 1
			mes += 1
		anno += 1
	return tecnicos

def run():
	equipos = [
		{
			"nombre":"Equipo 1",
			"jugadores":generar_jugadores(
				1998,
				[
					["arquero",2],["defensa",8],["medio campista",8],["delantero",5],
				]
			),
			"tecnicos":generar_tecnicos(
				1998,
				[
					["técnico",1],["asistente",2],["médico",2],["preparador",3],
				]
			)
		},
		{
			"nombre":"Equipo 2",
			"jugadores":generar_jugadores(
				1999,
				[
					["arquero",3],["defensa",8],["medio campista",7],["delantero",5],
				]
			),
			"tecnicos":generar_tecnicos(
				1998,
				[
					["técnico",1],["asistente",2],["médico",2],["preparador",3],
				]
			)
		},
		{
			"nombre":"Equipo 3",
			"jugadores":generar_jugadores(
				2000,
				[
					["arquero",4],["defensa",10],["medio campista",9],["delantero",6],
				]
			),
			"tecnicos":generar_tecnicos(
				1998,
				[
					["técnico",1],["asistente",2],["médico",2],["preparador",3],
				]
			)
		},
		{
			"nombre":"Equipo 4",
			"jugadores":generar_jugadores(
				2001,
				[
					["arquero",1],["defensa",6],["medio campista",5],["delantero",4],
				]
			),
			"tecnicos":generar_tecnicos(
				1998,
				[
					["técnico",1],["asistente",2],["médico",2],["preparador",3],
				]
			)
		},
		{
			"nombre":"Equipo 5",
			"jugadores":generar_jugadores(
				2000,
				[
					["arquero",2],["defensa",7],["medio campista",7],["delantero",3],
				]
			),
			"tecnicos":generar_tecnicos(
				1998,
				[
					["técnico",1],["asistente",2],["médico",2],["preparador",3],
				]
			)
		},
	]
	# ju = generar_tecnicos(
	# 			2000,
	# 			[
	# 				["arquero",2],
	# 				["defensa",8],
	# 				["medio campista",8],
	# 				["delantero",5],
	# 			]
	# 		)
	# ju = generar_tecnicos(
	# 			1998,
	# 			[
	# 				["técnico",1],["asistente",2],["médico",2],["preparador",3],
	# 			]
	# 		)
	# for j in ju:
	# 	print(j)
	Jugadores.objects.all().delete()
	Tecnicos.objects.all().delete()
	Equipo.objects.all().delete()
	for datos_equipo in equipos:
		if Equipo.objects.filter(nombre = datos_equipo["nombre"]).exists() == False:
			equipo = Equipo.objects.create(nombre = datos_equipo["nombre"])
			for jugador in datos_equipo["jugadores"]:
				Jugadores.objects.create(
					equipo = equipo,
					nombre = jugador["nombre"], 
					apellido = jugador["apellido"], 
					fecha_nacimiento = jugador["fecha_nacimiento"], 
					posicion = jugador["posicion"], 
					numero = jugador["numero"], 
					titular = jugador["titular"]
				)
			for tecnico in datos_equipo["tecnicos"]:
				Tecnicos.objects.create(
					equipo = equipo,
					nombre = tecnico["nombre"], 
					apellido = tecnico["apellido"], 
					fecha_nacimiento = tecnico["fecha_nacimiento"], 
					nacionalidad = tecnico["nacionalidad"], 
					rol = tecnico["rol"]
				)