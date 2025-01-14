from icecream import ic

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.base.models import LabUUID, Base
from apps.tabela.models import *
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

    cargo = models.ForeignKey('tabela.Cargo', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='colaboradores')
    turma = models.ForeignKey('tabela.MatriculaTurma', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='colaboradores')
    departamento = models.ForeignKey('tabela.Departamento', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='colaboradores')
    email = models.EmailField('email', max_length=254, unique=True, db_index=True)
    apelido = models.CharField(max_length=254, blank=True)
    cpf = models.CharField(max_length=50, blank=True)
    matricula = models.CharField(unique=True, max_length=254, blank=True)
    nivel = models.CharField(max_length=1, choices=TipoNivel.choices, default=TipoNivel.VISITANTE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    login = models.BooleanField(default=False)
    ferias = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'apelido']  

    objects = ColaboradorManager()

    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome.title()  

    def save(self, *args, **kwargs):
        if not self.matricula:  
            ano_atual = datetime.now().year 
            pkid_multiplicado = self.pkid * 3 if self.pkid else 0
            uuid_final = str(self.uuid).replace('-', '')[-4:]
            cpf_inicial = self.cpf[:3] if self.cpf else "000"

            self.matricula = f"{ano_atual}{pkid_multiplicado}{uuid_final}{cpf_inicial}"

        super().save(*args, **kwargs) 