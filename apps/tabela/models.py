from django.db import models

from apps.base.models import *


class Departamento(LabUUID, Base):

    class Meta:
        verbose_name = 'Departamento'

    def __str__(self):
        return self.nome


class Cargo(LabUUID, Base):

    class Meta:
        verbose_name = 'Cargo'

    def __str__(self):
        return self.nome


class Turma(LabUUID, Base):

    class Meta:
        verbose_name = 'Turma'

    def __str__(self):
        return self.nome


class HorarioEscolar(LabUUID, Base):

    class Meta:
        verbose_name = 'Horário Escolar'

    def __str__(self):
        return self.nome