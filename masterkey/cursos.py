from itertools import chain

from django.db.models import Count

from masterkey.models import Curso


def obtener_cursos(estudiante, fecha):
    maximoArribaAbajo = 7
    # if estudiante.nivel.nivel == 'A1':
    #     print "Estudiante A1"
    #     if (estudiante.nivel.leccion == 1) or (estudiante.nivel.leccion == 2) or (estudiante.nivel.leccion == 3) \
    #             or (estudiante.nivel.leccion == 4) or (estudiante.nivel.leccion == 5) \
    #             or (estudiante.nivel.leccion == 6) or (estudiante.nivel.leccion == 7) \
    #             or (estudiante.nivel.leccion == 8) or (estudiante.nivel.leccion == 9) \
    #             or (estudiante.nivel.leccion == 10):
    #         print "Dentro de 1 a 10"
    #         print (estudiante.nivel)
    #         cursos1 = Curso.objects.filter(sede__ciudad=estudiante.ciudad).filter(fecha=fecha).filter(
    #             capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).filter(max_tipo__gte=1)
    #
    #         cursos3 = Curso.objects.filter(sede__ciudad=estudiante.ciudad).filter(fecha=fecha).filter(
    #             capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).filter(max_tipo__lte=0).filter(
    #             tipo_estudiante__in=[estudiante.nivel])
    #
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2, cursos3))
    #         return cursos
    #
    #     if estudiante.nivel.leccion == 11:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 12:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 13:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 14:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 15:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 16) or (estudiante.nivel.leccion == 17) or (estudiante.nivel.leccion == 18) \
    #             or (estudiante.nivel.leccion == 19) or (estudiante.nivel.leccion == 20) \
    #             or (estudiante.nivel.leccion == 21) or (estudiante.nivel.leccion == 22) \
    #             or (estudiante.nivel.leccion == 23) or (estudiante.nivel.leccion == 24) \
    #             or (estudiante.nivel.leccion == 25) or (estudiante.nivel.leccion == 26) \
    #             or (estudiante.nivel.leccion == 27):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 28):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 29):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 30):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 31):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 32):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante).annotate(max_tipo__lte=Count('tipo_estudiante'))
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    # elif estudiante.nivel.nivel == 'A2':
    #     print ("Estudiante A2")
    #     if (estudiante.nivel.leccion == 1) or (estudiante.nivel.leccion == 2) or (estudiante.nivel.leccion == 3) \
    #             or (estudiante.nivel.leccion == 4) or (estudiante.nivel.leccion == 5) \
    #             or (estudiante.nivel.leccion == 6) or (estudiante.nivel.leccion == 7) \
    #             or (estudiante.nivel.leccion == 8) or (estudiante.nivel.leccion == 9) \
    #             or (estudiante.nivel.leccion == 10) or (estudiante.nivel.leccion == 11) \
    #             or (estudiante.nivel.leccion == 12) or (estudiante.nivel.leccion == 13) \
    #             or (estudiante.nivel.leccion == 14):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 15):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 16:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 17:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #
    #     if estudiante.nivel.leccion == 18:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #
    #     if estudiante.nivel.leccion == 19:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 20) or (estudiante.nivel.leccion == 21) or (estudiante.nivel.leccion == 22) \
    #             or (estudiante.nivel.leccion == 23) or (estudiante.nivel.leccion == 24):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 25):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 26):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 27):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 28):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 29:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    # elif estudiante.nivel.nivel == 'B1':
    #     print "Estudiante B1"
    #     if (estudiante.nivel.leccion == 1) or (estudiante.nivel.leccion == 2) or (estudiante.nivel.leccion == 3) \
    #             or (estudiante.nivel.leccion == 4) or (estudiante.nivel.leccion == 5):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #
    #     if (estudiante.nivel.leccion == 6):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 7):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 8):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 9):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 10):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 11) or (estudiante.nivel.leccion == 12) or (estudiante.nivel.leccion == 13) \
    #             or (estudiante.nivel.leccion == 14) or (estudiante.nivel.leccion == 15):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 16:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 17:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 18:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 19:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 20):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    # elif estudiante.nivel.nivel == 'B2':
    #     print "Estudiante B2"
    #     if (estudiante.nivel.leccion == 1) or (estudiante.nivel.leccion == 2) or (estudiante.nivel.leccion == 3) \
    #             or (estudiante.nivel.leccion == 4) or (estudiante.nivel.leccion == 5):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #
    #     if estudiante.nivel.leccion == 6:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 7:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 8:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 9:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 10:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if (estudiante.nivel.leccion == 11) or (estudiante.nivel.leccion == 12) or (estudiante.nivel.leccion == 13) \
    #             or (estudiante.nivel.leccion == 14) or (estudiante.nivel.leccion == 15):
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 16:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 17:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #
    #     if estudiante.nivel.leccion == 18:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 19:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    #     if estudiante.nivel.leccion == 20:
    #         cursos1 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(
    #             tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
    #                                    estudiante.nivel.leccion + maximoArribaAbajo)). \
    #             filter(tipo_nivel=estudiante.nivel.nivel).filter(sede__ciudad=estudiante.ciudad).exclude(
    #             tipo_nivel='xx').exclude(estudiantes=estudiante)
    #         cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
    #             filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad)
    #         cursos = list(chain(cursos1, cursos2))
    #         return cursos
    cursos1 = Curso.objects.filter(sede__ciudad=estudiante.ciudad).filter(fecha=fecha).filter(
        capacidad_maxima__gt=0). \
        filter(
        tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
                               estudiante.nivel.leccion + maximoArribaAbajo)). \
        filter(tipo_nivel=estudiante.nivel.nivel).exclude(
        tipo_nivel='xx').exclude(estudiantes=estudiante).filter(max_tipo__gte=1).order_by('hora_inicio')

    cursos3 = Curso.objects.filter(sede__ciudad=estudiante.ciudad).filter(fecha=fecha).filter(
        capacidad_maxima__gt=0). \
        filter(
        tipo_leccion__in=range(estudiante.nivel.leccion - maximoArribaAbajo,
                               estudiante.nivel.leccion + maximoArribaAbajo)). \
        filter(tipo_nivel=estudiante.nivel.nivel).exclude(
        tipo_nivel='xx').exclude(estudiantes=estudiante).filter(max_tipo__lte=0).filter(
        tipo_estudiante__in=[estudiante.nivel]).order_by('hora_inicio')

    cursos2 = Curso.objects.filter(fecha=fecha).filter(capacidad_maxima__gt=0). \
        filter(tipo_nivel='xx').filter(sede__ciudad=estudiante.ciudad).order_by('hora_inicio')
    cursos = list(chain(cursos1, cursos2, cursos3))

    return cursos


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
