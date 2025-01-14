from icecream import ic

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.colaborador.models import *
from apps.tabela.models import *

class DashboardMixin(LoginRequiredMixin):
    model = Colaborador

class Dashboard(DashboardMixin, ListView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user.pkid

        # Obter o colaborador relacionado ao usuário atual
        colaborador = Colaborador.objects.filter(pkid=user).first()
        
        if colaborador:
            # Obter todas as matrículas do colaborador
            matriculas = colaborador.matriculas.select_related('turma').all()

            # Estruturar os dados para o template
            turmas_info = []
            for matricula in matriculas:
                turma = matricula.turma
                ic(turma)
                materias = turma.materias.all()

                materias_info = []
                for materia in materias:
                    # Notas da matéria
                    notas = materia.notas.filter(matricula=matricula).all()
                    notas_dict = {nota.tipo: nota.valor for nota in notas}

                    # Frequências da matéria
                    frequencias = materia.frequencias.filter(matricula=matricula).all()
                    frequencias_list = [
                        {
                            'data': freq.data,
                            'presente': freq.presente,
                        }
                        for freq in frequencias
                    ]

                    materias_info.append({
                        'nome': materia.nome,
                        'professor': materia.professor.nome if materia.professor else "N/A",
                        'notas': notas_dict,
                        'frequencias': frequencias_list,
                        'horario': materia.horario if materia.horario else "00:00",
                    })
                ic(materias_info)

                turmas_info.append({
                    'turma_nome': turma.nome,
                    'materias': materias_info,
                    'situacao': matricula.get_status_display(),
                })
            
            context['turmas'] = turmas_info

        return context


class Frequencia(DashboardMixin, ListView):
    template_name = 'dashboard/frequencia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        turmas = Turma.objects.prefetch_related('materias__frequencias')
        for turma in turmas:
            print(f"Turma: {turma.nome}")
            for materia in turma.materias.all():
                print(f"  Matéria: {materia.nome}")
                for freq in materia.frequencias.all():
                    print(f"    Frequência: {freq.data}, Presente: {freq.presente}")
        context['turmas'] = turmas
        return context
