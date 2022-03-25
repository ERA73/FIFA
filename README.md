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
	* http://127.0.0.1/api/reporte/
		* Para el POST:
		* Para el PUT:
		* Para el DELETE:
    * http://127.0.0.1/api/jugadores/
		* Para el POST:
		* Para el PUT:
		* Para el DELETE:
    * http://127.0.0.1/api/tecnicos/
		* Para el POST:
		* Para el PUT:
		* Para el DELETE:
    * http://127.0.0.1/api/reporte/