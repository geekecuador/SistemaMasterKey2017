from django.contrib.auth.models import User
import csv
from masterkey.models import Estudiante, Programa, Ciudad, Nivel

f = open('a1SantoDomingo.csv', 'r')
with f:
	reader = csv.DictReader(f)
	for row in reader:
		print row[0]
		try:
			user = User.objects.create_user(row[4], password=row[5], email=row[6])
			user.is_superuser=False
			user.is_staff=False
			user.save()
			try:
				estudiante = Estudiante(cedula=row[0],usuario=User.objects.get(username=row[4]),
					programa=Programa.objects.get(id=1),ciudad=Ciudad.objects.get(nombre='Santo Domingo'),nivel=Nivel.objects.get(id=1),
					fecha_nacimiento=row[5], telefono = '0999999999',direccion_domicilio='ninguna', fecha_de_inicio=row[1],fecha_de_expiracion=row[2])
			except Exception as e:
				print "Error en el estudiante"
		except Exception as e:
			print "Error en el usuario"