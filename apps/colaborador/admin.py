# apps/colaborador/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Colaborador

@admin.register(Colaborador)
class ColaboradorAdmin(UserAdmin):
    # Quais campos aparecem na listagem do admin
    list_display = ('nome', 'email', 'uuid', 'cpf', 'matricula', 'nivel', 'turma', 'is_staff', 'is_active', 'login', 'ferias')
    list_filter = ('nivel', 'is_active', 'is_staff', 'login', 'ferias')
    search_fields = ('nome', 'email')
    ordering = ('email',)

    # Campos exibidos ao **editar** um usuário existente
    fieldsets = (
        (None, {
            'fields': ('email', 'password')  # em vez de "username", use "email"
        }),
        ('Informações Pessoais', {
            'fields': ('nome', 'apelido', 'cpf', 'matricula')
        }),
        ('Organização', {
            'fields': ('cargo', 'departamento')
        }),
        ('Informações da Turma', {
            'fields': ('turma',)
        }),
        ('Permissões e Status', {
            'fields': (
                'nivel',
                'is_staff',
                'is_active',
                'login',
                'ferias',
                'groups',
                'user_permissions',
            )
        }),
    )

    # Campos exibidos ao **criar** um novo usuário
    # (remova 'username' e use email/password1/password2)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'nome', 'apelido',
                'cargo', 'departamento',
                'nivel', 'is_staff', 'is_active', 'login', 'ferias',
                'groups', 'user_permissions',
            ),
        }),
    )

    # Se seu modelo não tem "username", também remover de filter_horizontal (se houver).
    filter_horizontal = ('groups', 'user_permissions')
