from personal.models import *

def run():
	equipos = [
		{"nombre":"Portugal"},
		{"nombre":"España"},
		{"nombre":"Alemania"},
		{"nombre":"Inglaterra"},
	]
	
	for equipo in equipos:
		if Equipo.objects.filter(nombre = equipo["nombre"]).exists() == False:
			Equipo.objects.create(nombre = equipo["nombre"])