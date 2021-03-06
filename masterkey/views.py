# -*- coding: utf-8 -*-
# coding=utf-8

from __future__ import print_function
from __future__ import unicode_literals

import datetime
import json

import xlwt
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View

from cursos import obtener_cursos, envioAlertaEmail
from models import Estudiante, Noticias, Taller, Test, Curso, Limitaciones, Ciudad, Estado, Sede, Nivel, Academic_Rank, \
    TallerRank, Seguimiento

from django.db import transaction


class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


def login_view(request):
    if request.user.is_authenticated():
        username = request.user

        try:
            estudiante = Estudiante.objects.get(usuario=username)

            return redirect('/tablero')
        except Exception:
            return redirect('/admin')

    else:
        error = False
        if request.method == 'GET':
            return render(request, 'page-login.html', {'error': error})
        elif request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                # Exitoso
                login(request, user)
                username = request.user
                estudiante = Estudiante.objects.get(usuario=username)
                fechaActual = datetime.datetime.now().date()
                fechaExpiracion = estudiante.fecha_de_expiracion
                if str(fechaExpiracion) > str(fechaActual):
                    return redirect('/tablero')
                else:
                    logout(request)
                    return render(request, 'alertas/vencimiento.html', {})

            else:
                # Fallido
                error = True
                return render(request, 'page-login.html', {'error': error})


def login_android(request):
    if request.user.is_authenticated():

        return redirect('/tablero')
    else:
        error = False
        if request.method == 'GET':
            return render(request, 'page-login.html', {'error': error})
        elif request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Exitoso
                login(request, user)
                return redirect('/tablero')
            else:
                # Fallido
                error = True
                return render(request, 'page-login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/')
def tablero(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
        estudiante = Estudiante.objects.get(usuario=username)
        noticias = Noticias.objects.filter(
            fecha__range=[datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=15)])
        return render(request, 'index.html', {'username': username, 'estudiante': estudiante, 'noticias': noticias})
    else:
        return redirect('/')


@login_required(login_url='/')
def paso1(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
        estudiante = Estudiante.objects.get(usuario=username)
        academico = Academic_Rank.objects.filter(nivel_id=999).filter(estudiante=estudiante)
        dt = datetime.datetime.now()
        start = dt - datetime.timedelta(days=dt.weekday())
        end = start + datetime.timedelta(days=6)
        limitacion = Limitaciones.objects.filter(fecha_reserva__range=[start, end]).filter(estudiante=estudiante)
        if len(academico) >= 1:
            return render(request, 'consulta1pasivo.html', {'username': username, 'estudiante': estudiante})
        elif len(limitacion) >= 3:
            return render(request, 'consulta1limitacion.html', {'username': username, 'estudiante': estudiante})
        else:
            return render(request, 'consulta1.html', {'username': username, 'estudiante': estudiante})
    else:
        return redirect('/')


@login_required(login_url='/')
@transaction.atomic()
def paso2(request):
    username = request.user
    estudiante = Estudiante.objects.get(usuario=username)
    if request.method == 'POST':
        if request.user.is_authenticated():
            fecha = request.POST['fecha_leccion']
            fecha = datetime.datetime.strptime(fecha, "%m/%d/%Y").strftime("%Y-%m-%d")
            cursos = obtener_cursos(estudiante, fecha)
            date = datetime.date.today()
            start_week = date - datetime.timedelta(date.weekday())
            end_week = start_week + datetime.timedelta(7)
            return render(request, 'consulta2.html',
                          {'username': username, 'estudiante': estudiante, 'cursos': cursos, 'fecha': fecha}, )
        else:
            return redirect('/tablero/')

    else:
        return redirect('/paso1/')


@login_required(login_url='/')
@transaction.atomic()
def paso3(request):
    username = None
    global estadocurso
    estadocurso = False

    if request.method == 'POST':
        if request.user.is_authenticated():
            username = request.user
            estudiante = Estudiante.objects.get(usuario=username)
            _curso = Curso.objects.get(pk=request.POST.getlist('id')[0])

            if _curso.tipo_nivel == 'xx' and _curso.tipo_leccion == 0 and _curso.max_tipo == 3:
                _curso.tipo_nivel = estudiante.nivel.nivel
                _curso.tipo_leccion = estudiante.nivel.leccion
                _curso.estudiantes.add(estudiante)
                _curso.tipo_estudiante.add(estudiante.nivel)
                _curso.capacidad_maxima = _curso.capacidad_maxima - 1
                if not estudiante.nivel in _curso.tipo_estudiante.all():
                    _curso.max_tipo = _curso.max_tipo - 1
                _curso.save()
                limitacion = Limitaciones(estudiante=estudiante, fecha_reserva=datetime.datetime.today())
                limitacion.save()
                envioAlertaEmail(estudiante)

                academico = Academic_Rank(estudiante=estudiante, nivel=Nivel.objects.get(pk=999),
                                          fecha=_curso.fecha, hora=_curso.hora_inicio, curso=_curso, firma_alumno=False)
                academico.save()
                estadocurso = True
                ctx = {
                    'nombres': estudiante.usuario.get_full_name(),

                    'curso': _curso,
                    'actividad': 'lección',
                }
                html_part = render_to_string('email/reservacion.html', ctx)
                send_mail('RESERVACIÓN ' + estudiante.usuario.get_full_name(), ' ', 'sistema@masterkey.com.ec',
                          [estudiante.usuario.email], fail_silently=False,
                          html_message=html_part)

            elif _curso.estudiantes.all().filter(
                    pk=estudiante.cedula).count() == 0 and _curso.tipo_estudiante.count() <= 3:
                _curso.estudiantes.add(estudiante)
                if not estudiante.nivel in _curso.tipo_estudiante.all():
                    _curso.max_tipo = _curso.max_tipo - 1
                _curso.capacidad_maxima = _curso.capacidad_maxima - 1
                _curso.tipo_estudiante.add(estudiante.nivel)
                _curso.save()
                estadocurso = True
                limitacion = Limitaciones(estudiante=estudiante, fecha_reserva=datetime.datetime.today())
                limitacion.save()
                envioAlertaEmail(estudiante)
                academico = Academic_Rank(estudiante=estudiante, nivel=Nivel.objects.get(pk=999),
                                          fecha=_curso.fecha, hora=_curso.hora_inicio, curso=_curso, firma_alumno=False)
                academico.save()
                ctx = {
                    'nombres': estudiante.usuario.get_full_name(),

                    'curso': _curso,
                    'actividad': 'lección',

                }
                html_part = render_to_string('email/reservacion.html', ctx)
                send_mail('RESERVACIÓN ' + estudiante.usuario.get_full_name(), ' ', 'sistema@masterkey.com.ec',
                          [estudiante.usuario.email], fail_silently=False,
                          html_message=html_part)

            return render(request, 'consulta3.html',
                          {'username': username, 'estudiante': estudiante, 'confirmacion': estadocurso,
                           'infoCurso': _curso})
        else:
            return redirect('/')
    elif request.method == 'GET':
        return redirect('/paso1/')


@login_required(login_url='/')
def registro(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
        estudiante = Estudiante.objects.get(usuario=username)
        return render(request, 'registro.html', {'username': username, 'estudiante': estudiante})
    else:
        return redirect('/')


@login_required(login_url='/')
def academic_rank(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
        estudiante = Estudiante.objects.get(usuario=username)
        academic_rank = Academic_Rank.objects.filter(estudiante=estudiante)
        return render(request, 'academic_rank.html',
                      {'username': username, 'estudiante': estudiante, 'academic_rank': academic_rank})
    else:
        return redirect('/')


@login_required(login_url='/')
def talleresRank(request):
    username = request.user
    estudiante = Estudiante.objects.get(usuario=username)
    talleresRank = TallerRank.objects.filter(estudiante=estudiante)
    return render(request, 'tallerRank.html',
                  {'username': username, 'estudiante': estudiante, 'talleresRank': talleresRank})


@login_required(login_url='/')
def test(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
        estudiante = Estudiante.objects.get(usuario=username)
        tests = Test.objects.filter(estudiante=estudiante)
        return render(request, 'test.html', {'username': username, 'estudiante': estudiante, 'tests': tests})
    else:
        return redirect('/')


@login_required(login_url='/')
def ver_talleres(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
        estudiante = Estudiante.objects.get(usuario=username)
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday())
        end_week = start_week + datetime.timedelta(7)
        _talleres = Taller.objects.filter(estudiantes=estudiante).filter(fecha__range=[start_week, end_week])
        return render(request, 'ver-talleres.html',
                      {'username': username, 'estudiante': estudiante, 'talleres': _talleres})
    else:
        return redirect('/')


@login_required(login_url='/')
def ver_lecciones(request):
    username = request.user
    estudiante = Estudiante.objects.get(usuario=username)
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    _lecciones = Curso.objects.filter(estudiantes=estudiante).filter(fecha__range=[start_week, end_week])
    return render(request, 'ver-lecciones.html',
                  {'username': username, 'estudiante': estudiante, 'lecciones': _lecciones})


@login_required(login_url='/')
def talleres(request):
    username = None
    if request.user.is_authenticated():
        if request.method == 'GET':
            username = request.user
            estudiante = Estudiante.objects.get(usuario=username)
            talleres = Taller.objects.filter(nivel__icontains=estudiante.nivel.nivel).filter(
                fecha__range=[datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=15)]).filter(
                capacidad__gt=0).filter(sede__ciudad=estudiante.ciudad).exclude(estudiantes=estudiante)
            return render(request, 'talleres.html',
                          {'username': username, 'estudiante': estudiante, 'talleres': talleres})
        elif request.method == 'POST':
            try:

                username = request.user
                estudiante = Estudiante.objects.get(usuario=username)
                taller = Taller.objects.get(pk=request.POST.getlist('value')[0])
                taller.estudiantes.add(estudiante)
                taller.capacidad = taller.capacidad - 1
                taller.save()
                _talleresRank = TallerRank(estudiante=estudiante, taller=taller, nota="", asistencia=False)
                _talleresRank.save()

                confirmacion = True
                ctx = {
                    'nombres': estudiante.usuario.get_full_name(),

                    'curso': taller,
                    'actividad': 'taller',
                }
                html_part = render_to_string('email/reservacion.html', ctx)
                send_mail('RESERVACIÓN ' + estudiante.usuario.get_full_name(), ' ', 'sistema@masterkey.com.ec',
                          [estudiante.usuario.email], fail_silently=False,
                          html_message=html_part)
                return render(request, 'confirmacion-talleres.html',
                              {'username': username, 'estudiante': estudiante, 'taller': taller,
                               'confirmacion': confirmacion})

            except Exception as e:
                confirmacion = False
                return render(request, 'confirmacion-talleres.html',
                              {'username': username, 'estudiante': estudiante, 'confirmacion': confirmacion})

    else:
        return redirect('/')


# Exportacion en formato excel

class ExportarEstudiantes(View):
    template_name = 'reportes/estudiantes.html'

    def get(self, request, *args, **kwargs):
        ciudad = Ciudad.objects.all()
        seguimiento = Estado.objects.all()
        return render(request, self.template_name, {'ciudad': ciudad, 'seguimiento': seguimiento})

    def post(self, request, *args, **kwargs):
        return exportar_estudiantes_xls(request.POST['estados'], request.POST['ciudades'])


class ExportarHorarios(StaffRequiredMixin, View):
    template_name = 'reportes/horarios.html'

    def get(self, request, *args, **kwargs):
        ciudad = Sede.objects.all()
        return render(request, self.template_name, {'ciudad': ciudad, })

    def post(self, request, *args, **kwargs):
        fecha = request.POST['fecha']
        sede = request.POST['sede']
        fecha = datetime.datetime.strptime(fecha, '%m/%d/%Y').date()
        return exportar_cursos_xls(fecha, sede)


class ExportarTalleres(StaffRequiredMixin, View):
    template_name = 'reportes/horarios.html'

    def get(self, request, *args, **kwargs):
        ciudad = Sede.objects.all()
        return render(request, self.template_name, {'ciudad': ciudad, })

    def post(self, request, *args, **kwargs):
        fecha = request.POST['fecha']
        sede = request.POST['sede']
        print(sede)
        # sede  = Sede.objects.get(pk=sede)
        # print(sede)
        fecha = datetime.datetime.strptime(fecha, '%m/%d/%Y').date()
        return exportar_talleres_xls(fecha, sede)


def exportar_estudiantes_xls(estado, ciudad):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Estudiantes_Activos')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Usuario', 'Nombre', 'Apellido', 'Email', 'Nivel', 'Lección', 'Contrato', 'Cédula', 'Inicio', 'Termino',
               'Fecha_Nacimiento', 'Teléfono', 'Observaciones','Estado']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # estudiantes_activos = Estudiante.objects.values_list('usuario__username', 'usuario__first_name',
    #                                                      'usuario__last_name', 'usuario__email',
    #                                                      'nivel__nivel', 'nivel__leccion', 'contrato', 'cedula',
    #                                                      'contrato__fecha_creacion', 'contrato__duracion',
    #                                                      'fecha_nacimiento', 'telefono',
    #                                                      'Estudiante__estado__seguimiento__comentario').filter(
    #     Estudiante__estado_id=estado).filter(ciudad_id=ciudad).distinct('usuario__email')
    print("Realizando la busqueda")
    estudiante_reporte = Seguimiento.objects.filter(estado_id=estado).filter(estudiante__ciudad_id=ciudad)

    print("Busqueda finalizada")
    for row in estudiante_reporte:
        row_num += 1
        ws.write(row_num, 0, str(row.estudiante.usuario), font_style)
        ws.write(row_num, 1, str(row.estudiante.usuario.first_name), font_style)
        ws.write(row_num, 2, str(row.estudiante.usuario.last_name), font_style)
        ws.write(row_num, 3, str(row.estudiante.usuario.email), font_style)
        ws.write(row_num, 4, str(row.estudiante.nivel.nivel), font_style)
        ws.write(row_num, 5, str(row.estudiante.nivel.leccion), font_style)
        ws.write(row_num, 6, str(row.estudiante.cedula), font_style)
        ws.write(row_num, 7, str(row.estudiante.fecha_de_inicio), font_style)
        ws.write(row_num, 8, str(row.estudiante.fecha_de_expiracion), font_style)
        ws.write(row_num, 9, str(row.estudiante.fecha_nacimiento), font_style)
        ws.write(row_num, 10,str(row.estudiante.telefono), font_style)
        ws.write(row_num, 11,str(row.comentario) , font_style)
        ws.write(row_num, 12, str(row.estado), font_style)
    wb.save(response)
    return response


def exportar_cursos_xls(fecha, sede):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="horarios.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Horarios' + str(fecha))

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Hora', 'Teacher', 'Book', 'Student']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    cursosExportar = Curso.objects.filter(sede_id=sede).filter(fecha=fecha).prefetch_related('estudiantes').order_by(
        'hora_inicio')
    for x in cursosExportar:
        row_num += 1
        ws.write(row_num, 0, str(x.hora_inicio), font_style)
        ws.write(row_num, 1, x.profesor.nombre, font_style)
        ws.write(row_num, 2, x.tipo_nivel, font_style)
        b = ""
        for a in x.estudiantes.prefetch_related('alumnos'):
            a = a.usuario.get_full_name() + ' ' + str(a.nivel.pk)
            b = b + ' ' + str(a) + ' | '
            print(b)
        ws.write(row_num, 3, b, font_style)
    wb.save(response)
    return response


def exportar_talleres_xls(fecha, sede):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="talleres.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Talleres ' + str(fecha))

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Hora', 'Teacher', 'Book', 'Students']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    talleresExportar = Taller.objects.filter(sede_id=sede).filter(fecha=fecha).prefetch_related('estudiantes').order_by(
        'hora_inicio')

    for x in talleresExportar:
        row_num += 1
        ws.write(row_num, 0, str(x.hora_inicio), font_style)
        ws.write(row_num, 1, x.profesor.nombre, font_style)
        ws.write(row_num, 2, x.nivel, font_style)
        b = ""
        for a in x.estudiantes.prefetch_related('alumnos'):
            a = a.usuario.get_full_name() + ' ' + str(a.nivel.pk)
            b = b + ' ' + str(a) + '| '
            print(b)
        ws.write(row_num, 3, b, font_style)
    wb.save(response)
    return response


def my_custom_page_not_found_view(request):
    return render(request, 'error/error404.html', {})


@staff_member_required()
@transaction.atomic()
def reservaciones(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        estudiante = Estudiante.objects.get(usuario__username=username)
        print(estudiante)
        fecha = request.POST['fecha_leccion']
        fecha = datetime.datetime.strptime(fecha, "%m/%d/%Y").strftime("%Y-%m-%d")
        cursos = obtener_cursos(estudiante, fecha)
        print(cursos)

        return render(request, 'reservaciones/resultados.html',
                      {'cursos': cursos, 'fecha': fecha, 'estudiante': estudiante})
    elif request.method == 'GET':
        return render(request, 'reservaciones/index.html', {})


@staff_member_required()
@transaction.atomic()
def reservacionesFinal(request):
    if request.method == 'POST':
        username = request.POST['username']
        estudiante = Estudiante.objects.get(usuario__username__exact=username)
        _curso = Curso.objects.get(pk=request.POST.getlist('id')[0])

        if _curso.tipo_nivel == 'xx' and _curso.tipo_leccion == 0 and _curso.max_tipo == 3 and _curso.estudiantes.all().filter(
                pk=estudiante.cedula).count() == 0:
            _curso.tipo_nivel = estudiante.nivel.nivel
            _curso.tipo_leccion = estudiante.nivel.leccion
            _curso.estudiantes.add(estudiante)
            _curso.tipo_estudiante.add(estudiante.nivel)
            _curso.capacidad_maxima = _curso.capacidad_maxima - 1
            _curso.max_tipo = _curso.max_tipo - 1
            _curso.save()
            envioAlertaEmail(estudiante)
            limitacion = Limitaciones(estudiante=estudiante, fecha_reserva=datetime.datetime.today())
            limitacion.save()

            academico = Academic_Rank(estudiante=estudiante, nivel=Nivel.objects.get(pk=999),
                                      fecha=_curso.fecha, hora=_curso.hora_inicio, curso=_curso, firma_alumno=False)
            academico.save()
            estadocurso = True
            ctx = {
                'nombres': estudiante.usuario.get_full_name(),

                'curso': _curso,
                'actividad': 'lección',
            }
            html_part = render_to_string('email/reservacion.html', ctx)
            send_mail('RESERVACIÓN ' + estudiante.usuario.get_full_name(), ' ', 'sistema@masterkey.com.ec',
                      [estudiante.usuario.email], fail_silently=False,
                      html_message=html_part)
            return render(request, 'reservaciones/final.html',
                          {'username': username, 'estudiante': estudiante, 'confirmacion': estadocurso,
                           'infoCurso': _curso})

        elif _curso.estudiantes.all().filter(
                pk=estudiante.cedula).count() == 0 and _curso.tipo_estudiante.count() <= 3:
            _curso.estudiantes.add(estudiante)

            if not estudiante.nivel in _curso.tipo_estudiante.all():
                _curso.max_tipo = _curso.max_tipo - 1

            _curso.capacidad_maxima = _curso.capacidad_maxima - 1
            _curso.tipo_estudiante.add(estudiante.nivel)
            _curso.save()
            estadocurso = True
            envioAlertaEmail(estudiante)
            limitacion = Limitaciones(estudiante=estudiante, fecha_reserva=datetime.datetime.today())
            limitacion.save()
            academico = Academic_Rank(estudiante=estudiante, nivel=Nivel.objects.get(pk=999),
                                      fecha=_curso.fecha, hora=_curso.hora_inicio, curso=_curso, firma_alumno=False)
            academico.save()
            ctx = {
                'nombres': estudiante.usuario.get_full_name(),

                'curso': _curso,
                'actividad': 'lección',
            }
            html_part = render_to_string('email/reservacion.html', ctx)
            send_mail('RESERVACIÓN ' + estudiante.usuario.get_full_name(), ' ', 'sistema@masterkey.com.ec',
                      [estudiante.usuario.email], fail_silently=False,
                      html_message=html_part)
            return render(request, 'reservaciones/final.html',
                          {'username': username, 'estudiante': estudiante, 'confirmacion': estadocurso,
                           'infoCurso': _curso})
        return render(request, 'reservaciones/final.html',
                      {'username': username, 'estudiante': estudiante, 'error': 'Existe un error, vuelva a intentar'})


def search(request):
    if request.is_ajax():
        q = request.GET['term']
        drugs = User.objects.filter(username__istartswith=q)
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json = drug.username
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


# cambios 2018

class ExportarEstudiantesPasivos(View):
    template_name = 'reportes/estudiantesPasivos.html'

    def get(self, request, *args, **kwargs):
        ciudad = Ciudad.objects.all()

        return render(request, self.template_name, {'ciudad': ciudad})

    def post(self, request, *args, **kwargs):
        return exportar_estudiantes_pasivos_xls(request.POST['ciudades'])


def exportar_estudiantes_pasivos_xls(ciudad):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="archivo_estudiantes_pasivos.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Estudiantes_Pasivos')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Usuario', 'Nombre', 'Apellido', 'Email', 'Nivel', 'Lección', 'Contrato', 'Cédula', 'Inicio', 'Termino',
               'Fecha_Nacimiento', 'Teléfono', 'Observaciones']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    estudiantes_activos = Estudiante.objects.values_list('usuario__username', 'usuario__first_name',
                                                         'usuario__last_name', 'usuario__email',
                                                         'nivel__nivel', 'nivel__leccion', 'contrato', 'cedula',
                                                         'contrato__fecha_creacion', 'contrato__duracion',
                                                         'fecha_nacimiento', 'telefono',
                                                         'Estudiante__estado__seguimiento__comentario').exclude \
        (academic_rank__curso__fecha__range=[datetime.datetime.now() - datetime.timedelta(days=90),
                                             datetime.datetime.now()]).filter \
        (ciudad_id=ciudad).distinct('usuario__email')

    # .values_list('user', 'first_name', 'last_name', 'email')
    # rows = User.objects.values()
    for row in estudiantes_activos:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
