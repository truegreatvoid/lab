from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from .settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('', include('apps.base.urls', namespace='base')),
    path('colaborador/', include('apps.colaborador.urls', namespace='colaborador')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('ceo-painel/', admin.site.urls),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)