from icecream import ic

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.colaborador.models import *

class ColaboradorMixin(LoginRequiredMixin):
    model = Colaborador

class Dashboard(ColaboradorMixin, ListView):
    template_name = 'colaborador/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context