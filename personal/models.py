from math import fabs
from django.db import models

class Equipo(models.Model):
	nombre = models.CharField(max_length=100, null=False, blank=False)
	imagen = models.TextField()
	escudo = models.TextField()

class Jugadores(models.Model):
	equipo = models.ForeignKey(Equipo, related_name='equipo_jugador', on_delete=models.CASCADE)
	foto = models.TextField()
	nombre = models.CharField(max_length=100, null=False, blank=False)
	apellido = models.CharField(max_length=100, null=False, blank=False)
	fecha_nacimiento = models.DateField(max_length=30, null=False, blank=False)
	pocision = models.CharField(max_length=30, null=False, blank=False)
	numero = models.IntegerField(null=False, blank=False, default=0)
	titular = models.BooleanField(default=False)

class Tecnicos(models.Model):
	choises = [
		("técnico", "técnico"),
		("asistente", "asistente"),
		("médico", "médico"),
		("preparador", "preparador")
	]
	
	equipo = models.ForeignKey(Equipo, related_name='equipo_tecnico', on_delete=models.CASCADE, null=False, blank=False)
	nombre = models.CharField(max_length=100, null=False, blank=False)
	apellido = models.CharField(max_length=100, null=False, blank=False)
	fecha_nacimiento = models.DateField(max_length=30, null=False, blank=False)
	nacionalidad = models.CharField(max_length=100, null=False, blank=False)
	roll = models.CharField(max_length=20, choices = choises, default="asistente")