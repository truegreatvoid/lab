from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('ceo-painel/', admin.site.urls),
    path('', include('apps.colaborador.urls', namespace='colaborador')),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)