from django.db import models
from django.utils.crypto import get_random_string

from apps.base.models import *
from apps.colaborador.models import *


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
    periodo = models.ForeignKey('tabela.Periodo', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='turmas')
    competencia = models.ForeignKey('tabela.Competencia', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='turmas')
    ensino = models.ForeignKey('tabela.Ensino', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='turmas')

    class Meta:
        verbose_name = 'Turma'

    def __str__(self):
        # return self.nome
        return f"{self.nome} {self.periodo} - {self.competencia}"


class Periodo(LabUUID, Base):
    class Meta:
        verbose_name = 'Período'

    def __str__(self):
        return self.nome


class Competencia(LabUUID, Base):
    class Meta:
        verbose_name = 'Competência'

    def __str__(self):
        return self.nome


class Ensino(LabUUID, Base):
    horario_inicio = models.TimeField(db_index=True)
    horario_fim = models.TimeField(db_index=True)

    class Meta:
        verbose_name = 'Ensino'

    def __str__(self):
        return self.nome


class Materia(LabUUID, Base):
    professor = models.ForeignKey('colaborador.Colaborador', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='materias')
    turma = models.ForeignKey('tabela.Turma', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='materias')
    horario = models.TimeField(db_index=True)
    cor = models.CharField(max_length=7, default='#' + get_random_string(6, '0123456789ABCDEF'))  


    class Meta:
        verbose_name = 'Matéria'

    def __str__(self):
        return self.nome

    @property
    def horario_formatado(self):
        return self.horario.strftime('%H:%M') if self.horario else "-"


class Nota(LabUUID):
    class TipoNota(models.TextChoices):
        AV1 = 'AV1', 'Avaliação 1'
        AV2 = 'AV2', 'Avaliação 2'
        AV3 = 'AV3', 'Avaliação 3'
        FINAL = 'FINAL', 'Prova Final'
        RECUPERACAO = 'REC', 'Recuperação'

    # aluno = models.ForeignKey('colaborador.Colaborador', on_delete=models.CASCADE, related_name='notas')
    matricula = models.ForeignKey('tabela.MatriculaTurma', on_delete=models.CASCADE, related_name='notas')
    materia = models.ForeignKey('tabela.Materia', on_delete=models.CASCADE, related_name='notas')
    tipo = models.CharField(max_length=10, choices=TipoNota.choices, default=TipoNota.AV1)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    descricao = models.CharField(max_length=255, blank=True)
    data = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'

    def __str__(self):
        return f"{self.matricula.aluno.nome} - {self.materia.nome} ({self.get_tipo_display()}): {self.valor}"


class Frequencia(LabUUID):
    # aluno = models.ForeignKey('colaborador.Colaborador', on_delete=models.CASCADE, related_name='frequencias')
    matricula = models.ForeignKey('tabela.MatriculaTurma', on_delete=models.CASCADE, related_name='frequencias')
    materia = models.ForeignKey('tabela.Materia', on_delete=models.CASCADE, related_name='frequencias')
    data = models.DateField() 
    presente = models.BooleanField(default=False) 

    class Meta:
        verbose_name = 'Frequência'
        verbose_name_plural = 'Frequências'

    def __str__(self):
        status = "Presente" if self.presente else "Ausente"
        return f"{self.matricula.aluno.nome} - {self.materia.nome} ({self.data}): {status}"


class MatriculaTurma(LabUUID, Base):

    class TipoStatus(models.TextChoices):
        MATRICULADO = 'M', 'Matriculado'
        TRANSFERIDO = 'T', 'Transferido'
        APROVADO = 'A', 'Aprovado'
        REPROVADO = 'R', 'Reprovado'


    nome = models.CharField('Nome', max_length=254, db_index=True, null=True, blank=True)
    aluno = models.ForeignKey('colaborador.Colaborador', on_delete=models.CASCADE, related_name='matriculas')
    turma = models.ForeignKey('tabela.Turma', on_delete=models.CASCADE, related_name='matriculas')
    quadro_horario = models.ForeignKey('tabela.QuadroHorario', on_delete=models.CASCADE, related_name='matriculas')
    data_matricula = models.DateField(auto_now_add=True)
    data_conclusao = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=TipoStatus.choices, default=TipoStatus.MATRICULADO)


    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'

    def __str__(self):
        return f"{self.aluno.nome} - {self.turma.nome} - {self.get_status_display()}"


class QuadroHorario(LabUUID, Base):
    pass
    '''
        professor turma dia_da_semana disciplina horario
    '''