from django.contrib.auth.models import User
import csv
from masterkey.models import Estudiante, Programa, Ciudad, Nivel

f = open('a1SantoDomingo.csv', 'r')
with f:
	reader = csv.DictReader(f)
	for row in reader:
		print row['usuario']
		try:
			user = User.objects.create_user(row['usuario'], password=row['password'],email=row['email'])
			user.is_superuser=False
			user.is_staff=False
			user.save()
		    try:
		    	estudiante = Estudiante(cedula='0500995972',usuario=User.objects.get(username=row['usuario']),
		    		programa=Programa.objects.get(id=1),ciudad=Ciudad.objects.get(nombre='Santo Domingo'),nivel=Nivel.objects.get(id=1),
		    		fecha_nacimiento=row['usuario'], telefono = '0999999999',direccion_domicilio='ninguna', fecha_de_inicio=row['inicio'],fecha_de_expiracion=row['terminacion'])
		    except Exception as e:
		    	print "Error en el estudiante"
		except Exception as e:
			print "Error en el usuario"