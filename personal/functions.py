from datetime import datetime, date

img_escudo = "data:image/png;base64, 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"
img_personal = "data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAHQAAADICAMAAAAOTDUbAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAEdUExURQAAAEBwv0Bwv0VwxURww0NzwkJywkRyxERyw0RyxENyxERyxURxxERzxENyxERyxERyxEh0xEt2xFB5xFN8xFR8xFh+w1l/w2GEwmeIw2uLw26MwnqUwoCYwYCYw4yewJGiv5alwJqowZuqxZ+rwaCswKCswaWvwKqyway0wqy0w7K3wLa5wLi7wrq6uru7u7u9v7u9wry8vLy+wL29vb2+wL6+vr+/v8DAwMDBwsHBwcLCwsPDw8TExMXFxcbGxsfHx8jIyMnJycrKyszMzM3Nzc7OztHR0dLS0tPT09TU1NXV1dbW1tfX19jY2Nvb29/f3+Dg4OLi4unp6erq6uvr6+zs7O3t7fT09PX19fb29vn5+fz8/P7+/v///y4d+XgAAAAQdFJOUwAQIDBAUGBwgI+fr7/P3+8jGoKKAAAACXBIWXMAABcRAAAXEQHKJvM/AAAD2ElEQVR4Xu2aeVvTQBDGDSlN0yZNPPFEEe+DelTA0gPw5FBR8Ua+/8ewaabSXDSzO7M+j8/8/iobdt7nnd3smRNoLLvqen4zGNL0G65TgXI+bMcPwjSN2gw8ZsCq+iCTwXPgf4ix3KzHSVx6u9MkI1wL/pmI6nTJCMok2w0IOhWfLMeVcjZjqlBJExfClaQG1XSw6hCsNB7UVMcq3ZxH6KqqaGqronMbo6XqQBA0dQigQBVCKDALIdDMYN7PFIHqKOFBACWaEASJcoPGKI3DlkZyI5QSXIPKyij0YJ1eBOCtahtVsKrbohHoVtXsujHYDqz1jo4JIFhJbKimCS6/JNnF5ldpGs3iQ7hyEPTdEZiVMFGThiFmd6UxkSbBNKriKiVLAwKWgagf4UQLt4RYMFN5E+pogxmTqN6YMISAZRBRPBCwDGSimN77T14Zkik8ArOTQm6+i8GszWahjjaYAb8CdbTBbN4sqKMNapFE1JNwyxWC9X0E7niHKL/Is2CSyQ2XXaJVEvbwjCK/+G0xwdoMs0CKIbBqQygE2lbxRvWtBgpGtXduiue+WlO5r3iLMAP1VQiUL6Y0plWl87IY5R7sQgAlFKc4T+9aSElVtRONsRRUdTWHoFU1cxuDXI8SXfNhhqZA411JYpcem3ylAbeAcmYDhya1Y0pcuQUe/lR5GvbxsoFHmdkJnMI1os/5AUClln1tA6/GZHKCWafuNUd79aDp1WsV2s4jCIIg/KeQHUPmUbBFJrgFP478WZ7gaOM4cq2SXeoVkbe8YDaaa5XsiLeYrFWyO71iMkeFBoxmrSpuuXGkrBoxmj7SN2I0dTdEdiUyjUmrhowmrBozOvl9qjGjE1YNGj2yatDocKcXaxo1OrZKdkNbjpFVsu9UyjK0ahk2OrJK9I0VhirdFyMR97orCbp34UGC4AT8oGF+HdSA9Xl4kIRWdO7R6nL7L8urT+fgQRJa0fBW79XONvDuZe8mFKcgFl3o7R+O+bLRX4DiFGyi39+2nwzMih7sdZb6W2adft1stXd/7fcMiv7cbrdefDs8NCn6aW2p8/Fg6NeYaP/D61Z760eUY3Oig3ZrY//3SNOY6OJmdy/K7IjPg0UoTkEsevH+m/fjIWl358ElKE5BLBqevvqsG4+8a8+vnYHCNNSiYXj+9qCzstJZv3MBCrLQi4YnLz8c9B9fOQV/5sAgGoZnr984Bz9zYRGdhoiyIqKsiCgrIsqKiLIioqyIKCsiyoqIsiKirIgoKyLKioiyIqKsiCgrIsqKiLIioqyIKCsiyoqIsiKirIgoKyLKSBj+AZYdYjXiLWgzAAAAAElFTkSuQmCC"

def validate_parameters(fields, group_params):
	for key in fields:
		is_ok = False
		for params in group_params:
			is_ok = is_ok or key in params
		if not is_ok:
			raise Exception(f"Clave [{key}]: Requerida")

def validate_model_list(query_result, elemento = None):
	if query_result.count() > 0:
		return query_result
	objeto = f' {elemento} ' if elemento else ' '
	raise Exception(f"El elemento buscado{objeto}no existe, contacte con el administrador")

def get_parameter(key, group_params, param_type = None, allow_empty = True):
	for params in group_params:
		if key in params:
			if param_type:
				if isinstance(params[key], param_type):
					if param_type == list:
						if len(params[key]) == 0 and allow_empty == False:
							raise Exception(f"Clave [{key}]: Sin datos")
				else:
					raise Exception(f"Clave [{key}]: Tipo incorrecto")
			elif not allow_empty:
				if len(params[key]) == 0:
					raise Exception(f"Clave [{key}]: Sin datos")
			return params[key]
	raise Exception(f"Clave [{key}]: Requerida")

def validate_type(commands, mensaje):
	try:
		if commands[0] == 'fecha':
			fecha = datetime.strptime(commands[1], '%Y-%m-%d').date()
			return fecha
		elif commands[0] == 'text':
			return commands[1] if len(commands[1]) > 0 else 1/0
	except:
		raise Exception(mensaje)

def calcular_edad(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def is_double(valor):
	try:
		nuevo = float(valor)
		return True
	except:
		return False