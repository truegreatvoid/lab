from icecream import ic

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.base.models import LabUUID, Base
from apps.tabela.models import Cargo, Departamento
from apps.colaborador.manager import *

class Colaborador(AbstractBaseUser, PermissionsMixin, LabUUID, Base):

    class TipoNivel(models.TextChoices):
        ADMINISTRADOR = 'A', 'Administrador'
        BIBLIOTECARIO = 'B', 'Bibliotecário'
        COORDENADOR = 'C', 'Coordenador'
        DIRETOR = 'D', 'Diretor'
        PROFESSOR = 'P', 'Professor'
        ALUNO = 'O', 'Aluno'
        TI = 'T', 'TI'
        SECRETARIA = 'S', 'Secretária'
        VISITANTE = 'V', 'Visitante'

    cargo = models.ForeignKey(Cargo, on_delete=models.DO_NOTHING, null=True, blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, null=True, blank=True)
    email = models.EmailField('email', max_length=254, unique=True, db_index=True)
    apelido = models.CharField(max_length=254, blank=True)
    nivel = models.CharField(max_length=1, choices=TipoNivel.choices, default=TipoNivel.VISITANTE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    login = models.BooleanField(default=False)
    ferias = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'apelido']  # ajuste se 'nome' vier da classe Base

    objects = ColaboradorManager()

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome.title()  # se 'nome' realmente existir em Base
