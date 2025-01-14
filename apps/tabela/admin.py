# apps/tabela/admin.py
from django.contrib import admin
from .models import *

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    pass


@admin.register(Competencia)
class CompetenciaAdmin(admin.ModelAdmin):
    pass


@admin.register(Ensino)
class EnsinoAdmin(admin.ModelAdmin):
    pass


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    pass


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    pass


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    pass


@admin.register(MatriculaTurma)
class MatriculaTurmaAdmin(admin.ModelAdmin):
    pass