# coding=utf-8
from itertools import chain

from django.core.mail import send_mail
from django.template.loader import render_to_string

from masterkey.models import Curso, Academic_Rank


def obtener_cursos(estudiante, fecha):
    maximoArribaAbajo = 7
    import datetime
    fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d").strftime("%Y-%m-%d")
    fechaActual = str(datetime.date.today())
    academico = Academic_Rank.objects.filter(nivel_id=999).filter(estudiante=estudiante)
    academico.count()
    if (fecha > fechaActual) and len(academico) >= 1 :

        # CURSOS NO VACIOS
        cursos1 = Curso.objects.filter(sede__ciudad=estudiante.ciudad).filter(fecha=fecha).filter(
            capacidad_maxima__gt=0). \
            filter(
            tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
                                   estudiante.nivel.leccion + maximoArribaAbajo)). \
            filter(tipo_nivel=estudiante.nivel.nivel).exclude(
            tipo_nivel='xx').exclude(estudiantes=estudiante).filter(max_tipo__gt=0).order_by('hora_inicio')

        cursos3 = Curso.objects.filter(sede__ciudad=estudiante.ciudad).filter(fecha=fecha).filter(
            capacidad_maxima__gt=0). \
            filter(
            tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
                                   estudiante.nivel.leccion + maximoArribaAbajo)). \
            filter(tipo_nivel=estudiante.nivel.nivel).exclude(
            tipo_nivel='xx').exclude(estudiantes=estudiante).filter(max_tipo__exact=0).filter(tipo_estudiante__in=[estudiante.nivel]).order_by('hora_inicio')

        # cursos3 = Curso.objects.filter(sede__ciudad=estudiante.ciudad).filter(fecha=fecha).filter(
        #     capacidad_maxima__gt=0). \
        #     filter(
        #     tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
        #                            estudiante.nivel.leccion + maximoArribaAbajo)). \
        #     filter(tipo_nivel=estudiante.nivel.nivel).exclude(
        #     tipo_nivel='xx').exclude(estudiantes=estudiante).filter(max_tipo__lte=0).filter(
        #     tipo_estudiante__in=[estudiante.nivel]).order_by('hora_inicio')

        # CURSOS VACIOS
        cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
            filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad).order_by('hora_inicio')

        cursos = list(chain(cursos1, cursos2,cursos3))

        return cursos
    else:
        cursos = list()
        return cursos

    # Curso para la sede.

    cursossede = Curso.objects.filter(sede__ciudad=estudiante.ciudad).filter(fecha=fecha).filter(capacidad_maxima__gt=0)

    #


def inactivo(estudiante):
    if estudiante.nivel.nivel == 'A1':
        if (estudiante.nivel.leccion == 15) or (estudiante.nivel.leccion == 32):
            usuario = estudiante.usuario
            usuario.is_active = False
            usuario.save()

    elif estudiante.nivel.nivel == 'A2':
        if (estudiante.nivel.leccion == 19) or (estudiante.nivel.leccion == 29):
            usuario = estudiante.usuario
            usuario.is_active = False
            usuario.save()

    elif estudiante.nivel.nivel == 'B1':
        if (estudiante.nivel.leccion == 10) or (estudiante.nivel.leccion == 20):
            usuario = estudiante.usuario
            usuario.is_active = False
            usuario.save()

    elif estudiante.nivel.nivel == 'B2':
        if (estudiante.nivel.leccion == 10) or (estudiante.nivel.leccion == 20):
            usuario = estudiante.usuario
            usuario.is_active = False
            usuario.save()


def envioAlertaEmail(estudiante):
    id = [15, 32, 51, 61, 71, 81, 91, 101]
    if (estudiante.nivel.id in id):
        ctx = {
            'nombres': estudiante.usuario.get_full_name(),
        }
        html_part = render_to_string('email/recordatorio.html', ctx)
        send_mail('RECORDATORIO: ' + estudiante.usuario.get_full_name(), ' ', 'sistema@masterkey.com.ec',
                  [estudiante.usuario.email], fail_silently=False,
                  html_message=html_part)
