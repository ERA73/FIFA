# Pasos para iniciar el proyecto

Dentro de la carpeta del proyecto:

* crear entorno virtual 
	```
	virtualenv env
	```
* activar entorno virtual
	```
	env/Scripts/activate
	```
* instalar dependencias
	```
	pip install -r Requirements.txt
	```
* (Opcional) crear usuario administrador:
	```
	python manage.py createsuperuser --email admin@example.com --username admin
	```
	ó
	```
	python manage.py createsuperuser
	```
* migrar por primera vez:
	```
	python manage.py migrate
	```
* migrar modelos del programa y migrar:
	```
	python manage.py makemigrations personal
	python manage.py migrate
	```
* (opcional) generar datos de prueba:
	```
	python manage.py runscript initial_data
	```
* Iniciar el servidor:
	```
	python manage.py runserver 0.0.0.0:80
	```

# Manual

* Rutas:
	* http://127.0.0.1/api/equipos/ Retorna la lista de equipos
		* Para la peticion POST de un nuevo equipo:
		http://127.0.0.1/api/equipos/\<id>
		* Para las peticiones GET, PUT y DELETE de un equipo especifico:
		http://127.0.0.1/api/equipos/\<id>
		```
		Para POST y PUT enviar por Body:
		{
			"nombre":"nombre",
			"imagen":"imagen",
			"escudo":"escudo"
		}
		```
    * http://127.0.0.1/api/jugadores/ Retorna la lista de jugadores
		* Para la peticion POST de un nuevo jugador:
		http://127.0.0.1/api/jugadores/
		* Para las peticiones GET, PUT y DELETE de un jugador especifico:
		http://127.0.0.1/api/jugadores/\<id>
		```
		Para POST y PUT enviar por Body:
		{
			"id_equipo": 40,
			"nombre": "nombre",
			"apellido": "apellido",
			"fecha_nacimiento": "2000-02-03",
			"posicion": "posicion",
			"numero": 21,
			"foto": "foto",
			"titular":0
		}
		```
    * http://127.0.0.1/api/tecnicos/ Retorna la lista de técnicos
		* Para la peticion POST de un nuevo tecnico:
		http://127.0.0.1/api/tecnicos/
		* Para las peticiones GET, PUT y DELETE de un tecnico especifico:
		http://127.0.0.1/api/tecnicos/\<id>
		```
		Para POST y PUT enviar por Body:
		{
			"id_equipo": 41,
			"nombre": "nombre1",
			"apellido": "apellido1",
			"fecha_nacimiento": "2000-01-01",
			"nacionalidad": "nacionalidad",
			"rol": "asistente"
		}
		```
    * http://127.0.0.1/api/reporte/