from django.urls import path
from .views import (
    AcidezOleoDegomadoCreateView,
    AcidezOleoDegomadoListView,
    AnaliseHomeView,
    UmidadeCreateView, ProteinaCreateView, OleoDegomadoCreateView,
    UmidadeListView, ProteinaListView, OleoDegomadoListView
)

app_name = 'analises'

urlpatterns = [
    path('', AnaliseHomeView.as_view(), name='home'),
    path('umidade/nova/', UmidadeCreateView.as_view(), name='umidade_create'),
    path('proteina/nova/', ProteinaCreateView.as_view(), name='proteina_create'),
    path('oleo/nova/', OleoDegomadoCreateView.as_view(), name='oleo_create'),
    path('umidade/', UmidadeListView.as_view(), name='umidade_list'),
    path('proteina/', ProteinaListView.as_view(), name='proteina_list'),
    path('oleo/', OleoDegomadoListView.as_view(), name='oleo_list'),
    path('oleoAcidez/', AcidezOleoDegomadoListView.as_view(), name='acidez_list'),
    path('oleoAcidez/nova/', AcidezOleoDegomadoCreateView.as_view(), name='acidez_create')
]