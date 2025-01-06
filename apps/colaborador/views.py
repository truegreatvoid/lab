from icecream import ic

from django.views.generic import ListView

from apps.colaborador.models import *

class Dashboard(ListView):
    model = Colaborador
    template_name = 'colaborador/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context