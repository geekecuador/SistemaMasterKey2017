# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
# Create your models here.
from django.db.models.signals import post_save
from django.template.loader import render_to_string


class Ciudad(models.Model):
    nombre = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'ciudad'
        verbose_name_plural = 'ciudades'

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    estado = models.CharField(max_length=35)

    class Meta:
        verbose_name = 'estado'
        verbose_name_plural = 'estados'

    def __str__(self):
        return "%s" % str(self.estado)


class Programa(models.Model):
    nombre_del_programa = models.CharField(max_length=25)

    def __str__(self):
        return self.nombre_del_programa


class Sede(models.Model):
    nombre_sede = models.CharField(max_length=20)
    ciudad = models.ForeignKey(Ciudad)
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return self.nombre_sede


class Nivel(models.Model):
    nivel = models.CharField(max_length=2)
    leccion = models.IntegerField()
    tema = models.CharField(u"Actividad", max_length=35)

    class Meta:
        ordering = ['nivel']
        verbose_name = 'nivel'
        verbose_name_plural = 'niveles'

    def __str__(self):
        return self.nivel + " " + str(self.leccion) + "--" + self.tema


class Estudiante(models.Model):
    cedula = models.CharField(u"cédula", max_length=11, primary_key=True)
    usuario = models.OneToOneField(User, unique=True, )
    foto = models.ImageField(upload_to='estudiante_perfil/', default='estudiante_perfil/master.jpg')
    fecha_nacimiento = models.DateField(u'fecha de nacimiento', blank=True, null=True)
    telefono = models.CharField(u'telefono', max_length=10)
    direccion_domicilio = models.CharField(max_length=25, blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    programa = models.ForeignKey(Programa)
    fecha_de_inicio = models.DateField()
    fecha_de_expiracion = models.DateField()
    lugar_de_trabajo = models.CharField(max_length=30, blank=True)
    contacto_de_emergencia = models.CharField(max_length=30, blank=True)
    relacion_de_contacto_de_emergencia = models.CharField(u'relación de contacto de emergencia', max_length=30,
                                                          blank=True)
    telefono_de_contanto_de_emergencia = models.CharField(u'teléfono de contacto de emergencia', max_length=10,
                                                          blank=True)
    ciudad = models.ForeignKey(Ciudad)
    nivel = models.ForeignKey(Nivel)

    def __str__(self):
        return str(self.usuario.get_full_name().encode(
            'utf-8')) + " | " + str(self.nivel.nivel) + " " + str(self.nivel.leccion) + " - " + str(self.nivel.tema)


class Contrato(models.Model):
    numero_contrato = models.CharField(max_length=8, primary_key=True)
    numero_factura = models.CharField(max_length=10, blank=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(u'Fecha de nacimiento', blank=True, null=True)
    cedula = models.CharField(u"Cédula", max_length=10, blank=True)
    email = models.EmailField('e-mail', blank=True)
    direccion_domicilio = models.TextField(blank=True)
    telefono = models.CharField(max_length=10, blank=True)
    celular = models.CharField(max_length=10, blank=True)
    empresa = models.CharField(max_length=30, blank=True)
    cargo = models.CharField(max_length=20, blank=True)
    direccion_empresa = models.CharField(max_length=30, blank=True)
    telefono_empresa = models.CharField(max_length=10, blank=True)
    fecha_creacion = models.DateField(u'Fecha de creación')
    duracion = models.DateField()
    sede_firma_contrato = models.ForeignKey(Sede)
    beneficiarios = models.ManyToManyField(Estudiante)

    def __str__(self):
        return self.numero_contrato + ' ' + self.nombre + ' ' + self.apellidos


class Profesor(models.Model):
    cedula = models.CharField(u"Cédula", max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sede = models.ForeignKey(Sede)
    horario_lunes_inicio_manana = models.TimeField(blank=True, null=True)
    horario_lunes_fin_manana = models.TimeField(blank=True, null=True)
    horario_lunes_inicio_tarde = models.TimeField(blank=True, null=True)
    horario_lunes_fin_tarde = models.TimeField(blank=True, null=True)
    horario_martes_inicio_manana = models.TimeField(blank=True, null=True)
    horario_martes_fin_manana = models.TimeField(blank=True, null=True)
    horario_martes_inicio_tarde = models.TimeField(blank=True, null=True)
    horario_martes_fin_tarde = models.TimeField(blank=True, null=True)
    horario_miercoles_inicio_manana = models.TimeField(blank=True, null=True)
    horario_miercoles_fin_manana = models.TimeField(blank=True, null=True)
    horario_miercoles_inicio_tarde = models.TimeField(blank=True, null=True)
    horario_miercoles_fin_tarde = models.TimeField(blank=True, null=True)
    horario_jueves_inicio_manana = models.TimeField(blank=True, null=True)
    horario_jueves_fin_manana = models.TimeField(blank=True, null=True)
    horario_jueves_inicio_tarde = models.TimeField(blank=True, null=True)
    horario_jueves_fin_tarde = models.TimeField(blank=True, null=True)
    horario_viernes_inicio_manana = models.TimeField(blank=True, null=True)
    horario_viernes_fin_manana = models.TimeField(blank=True, null=True)
    horario_viernes_inicio_tarde = models.TimeField(blank=True, null=True)
    horario_viernes_fin_tarde = models.TimeField(blank=True, null=True)
    horario_sabado_inicio_manana = models.TimeField(blank=True, null=True)
    horario_sabado_fin_manana = models.TimeField(blank=True, null=True)
    horario_sabado_inicio_tarde = models.TimeField(blank=True, null=True)
    horario_sabado_fin_tarde = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre + " " + self.apellido

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'


class Taller(models.Model):
    tema = models.CharField(max_length=30)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    capacidad = models.IntegerField()
    profesor = models.ForeignKey(Profesor)
    sede = models.ForeignKey(Sede)
    nivel = models.CharField(max_length=12)
    estudiantes = models.ManyToManyField(Estudiante, related_name='alumnos', blank=True)

    class Meta:
        verbose_name = 'taller'
        verbose_name_plural = 'talleres'

    def __str__(self):
        return self.tema


class Curso(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    capacidad_maxima = models.PositiveSmallIntegerField(default=6)
    sede = models.ForeignKey(Sede)
    profesor = models.ForeignKey(Profesor)
    estudiantes = models.ManyToManyField(Estudiante, blank=True)
    tipo_nivel = models.TextField(max_length='2', default='xx')
    tipo_leccion = models.PositiveSmallIntegerField(default=0)
    max_tipo = models.SmallIntegerField(default=3)
    tipo_estudiante = models.ManyToManyField(Nivel, related_name='tipo_estudiante', blank=True)

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.id is not None:
            print("SAVE")
            estudiantes = self.estudiantes.all()
            lista = []
            for estudiante in estudiantes:
                lista.append(estudiante.nivel_id)
                lista = list(set(lista))
                if len(lista) >= 3:
                    return
                else:
                    super(Curso, self).save()
        else:
            super(Curso, self).save()

    def __str__(self):
        return "Sede:"+self.sede.nombre_sede+ "Fecha: " + str(self.fecha) + " Hora Inicio: " + str(self.hora_inicio) + \
               " Capacidad: " + str(self.capacidad_maxima)


class Academic_Rank(models.Model):
    EXC = 'Excellent'
    VG = 'Very Good'
    G = 'Good'
    OK = 'Work at home'
    R = 'Repeat'
    CONT = 'Continue'
    NS = 'No Show'
    ACADEMIC_RANK_CHOICES = (
        (EXC, 'Excellent'),
        (VG, 'Very Good'),
        (G, 'Good'),
        (OK, 'Work at home'),
        (R, 'Repeat'),
        (CONT, 'Continue'),
        (NS, 'No Show'),
    )
    estudiante = models.ForeignKey(Estudiante)
    nivel = models.ForeignKey(Nivel)
    fecha = models.DateField()
    hora = models.TimeField()
    nota = models.CharField(max_length=15,
                            choices=ACADEMIC_RANK_CHOICES,
                            blank=True)
    comentarios = models.CharField(max_length=35, blank=True)
    firma_alumno = models.BooleanField(blank=True)
    curso = models.ForeignKey(Curso)

    class Meta:
        verbose_name = 'record académico'
        verbose_name_plural = 'records académicos'

    def __str__(self):
        return self.estudiante.cedula

class TallerRank(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    taller = models.ForeignKey(Taller)
    nota = models.CharField(max_length=35, blank=True)
    asistencia = models.BooleanField(blank=True)


    class Meta:
        verbose_name = 'rank talleres'
        verbose_name_plural = 'ranks de talleres'

    def __str__(self):
        return self.estudiante.usuario.get_full_name() + " "+self.taller.tema


class Limitaciones(models.Model):
    estudiante = models.ForeignKey(Estudiante)
    fecha_reserva = models.DateField()

    class Meta:
        verbose_name = 'limitación'
        verbose_name_plural = 'limitaciones'

    def __str__(self):
        return "%s" % str(self.estudiante.usuario.get_full_name())


class Test(models.Model):
    tema = models.CharField(max_length=35, blank=True)
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True)
    estudiante = models.ForeignKey(Estudiante, blank=True)
    profesor = models.ForeignKey(Profesor, blank=True)
    sede = models.ForeignKey(Sede, blank=True)

    def __str__(self):
        return "%s" % (str(self.estudiante.usuario.get_full_name()))


class Noticias(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateField()

    class Meta:
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'

    def __str__(self):
        return "%s %s" % (self.titulo, str(self.fecha))


class Seguimiento(models.Model):
    AC = 'Activo'
    IN = 'Inactivo'
    VC = 'Vencido'
    CB = 'Cambio de beneficiario'
    CG = 'Congelado'
    BQ = 'Bloqueado'
    PJ = 'Prejurídico'
    RC = 'Recesión de contrato'
    TM = 'Terminado'

    estudiante = models.OneToOneField('Estudiante', related_name='Estudiante', unique=True)
    estado = models.ForeignKey(Estado)
    comentario = models.TextField()

    class Meta:
        verbose_name = 'seguimiento'
        verbose_name_plural = 'seguimientos'

    def __str__(self):
        return "%s -  %s-  %s" % (self.estudiante, self.comentario, self.estado)


# Descomentar en produccion
def send_user_email(sender, instance, **kwargs):
    if kwargs['created']:
        estudiante = Estudiante.objects.get(pk=instance.pk)
        ctx = {
            'usuario': estudiante.usuario.get_username(),
            'password': 'masterkey',
            'nombres': estudiante.usuario.get_full_name(),

        }
        if estudiante.ciudad.nombre == 'Esmeraldas':
            html_part = render_to_string('email/bienvenidaEsmeraldas.html', ctx)
            send_mail('BIENVENIDA ' + estudiante.usuario.get_full_name(), ' ', 'sistema@masterkey.com.ec',
                      [estudiante.usuario.email], fail_silently=False,
                      html_message=html_part)
        elif estudiante.ciudad.nombre == 'Santo Domingo':
            html_part = render_to_string('email/bienvenidaSantoDomingo.html', ctx)
            send_mail('BIENVENIDA ' + estudiante.usuario.get_full_name(), ' ', 'sistema@masterkey.com.ec',
                      [estudiante.usuario.email], fail_silently=False,
                      html_message=html_part)


post_save.connect(send_user_email, sender=Estudiante)


def activateUser(sender, instance, **kwargs):
    if kwargs['created']:
        test = Test.objects.get(pk=instance.pk)
        estudiante = test.estudiante
        usuario = estudiante.usuario
        usuario.is_active = True
        usuario.save()


post_save.connect(activateUser, sender=Test)
