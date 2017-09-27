# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from daterange_filter.filter import DateRangeFilter
from django.contrib import admin

from actions import export_as_csv_action
import models


# Register your models here.


@admin.register(models.Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ('nombre_sede', 'ciudad', 'direccion', 'telefono', 'hora_inicio', 'hora_fin')


@admin.register(models.Nivel)
class NivelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nivel', 'leccion', 'tema')
    list_editable = ('leccion', 'nivel', 'tema')
    list_filter = ('nivel',)
    ordering = ('leccion',)
    search_fields = ('tema',)
    actions = [export_as_csv_action("Exportar a Excel", fields=['id', 'nivel', 'tema', ])]


class Academic_RankInline(admin.TabularInline):
    model = models.Academic_Rank
    ordering = ('fecha',)
    fk_name = "estudiante"
    extra = 1
    search_fields = ('nivel', 'leccion',)


class SeguimientoInline(admin.TabularInline):
    model = models.Seguimiento

@admin.register(models.Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'ciudad', 'nivel', 'fecha_de_inicio',
                    'fecha_de_expiracion')
    list_filter = ('ciudad', 'nivel')
    list_editable = ('nivel',)
    search_fields = ('cedula',)
    raw_id_fields = ('usuario', 'nivel')
    inlines = [Academic_RankInline, SeguimientoInline]


@admin.register(models.Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = (
        'numero_contrato', 'numero_factura', 'nombre', 'apellidos', 'cedula', 'email', 'telefono', 'celular',
        'fecha_creacion', 'duracion', 'sede_firma_contrato')
    list_filter = ('sede_firma_contrato', ('fecha_creacion', DateRangeFilter),)
    search_fields = ('numero_contrato', 'nombre', 'apellidos',)
    filter_horizontal = ('beneficiarios',)


@admin.register(models.Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'apellido', 'sede')
    list_filter = ('sede',)
    search_fields = ('nombre',)


@admin.register(models.Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ('tema', 'fecha', 'hora_inicio', 'hora_fin', 'capacidad', 'profesor', 'lugar', 'nivel',)
    filter_horizontal = ('estudiantes',)
    list_filter = ('lugar',)
    actions = [export_as_csv_action("Exportar a Ecxel",
                                    fields=['tema', 'fecha', 'hora_inicio', 'hora_fin', 'capacidad', 'profesor',
                                            'lugar', 'nivel', ])]


@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = (
        'fecha', 'hora_inicio', 'hora_fin', 'capacidad_maxima', 'sede', 'profesor', 'tipo_nivel', 'tipo_leccion',
        'max_tipo',)
    list_editable = ('profesor',)
    list_filter = ('sede', ('fecha', DateRangeFilter), 'hora_inicio',)
    filter_horizontal = ('estudiantes', 'tipo_estudiante',)
    actions = [export_as_csv_action("Exportar a Ecxel",
                                    fields=['fecha', 'hora_inicio', 'hora_fin', 'sede', 'profesor', 'tipo_nivel', ])]


@admin.register(models.Seguimiento)
class SeguimientoAdmin(admin.ModelAdmin):
    list_display = ( 'estudiante','comentario', 'estado',)
    list_filter = ('estado',)
    list_editable = ('estado',)
    # raw_id_fields = ('estudiante',)


@admin.register(models.Academic_Rank)
class Academic_RankAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'nivel', 'fecha', 'hora', 'nota', 'comentarios', 'firma_alumno', 'profesor',)
    raw_id_fields = ('nivel', 'estudiante')
    search_fields = ['nivel', 'estudiante', ]


@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    raw_id_fields = ('estudiante',)
    search_fields = ['estudiante__apellido', 'estudiante__nombre', ]
    list_filter = ('estudiante',)



@admin.register(models.Limitaciones)
class LimitacionesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Programa)
class ProgramaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    pass

# Quitar en producción
@admin.register(models.Estado)
class EstadoAdmin(admin.ModelAdmin):
    pass


