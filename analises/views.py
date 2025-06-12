from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from .models import AnaliseUmidade, AnaliseProteina, AnaliseUmidadeOleoDegomado
from .forms import AnaliseUmidadeForm, AnaliseProteinaForm, AnaliseUmidadeOleoDegomadoForm

class AnaliseHomeView(TemplateView):
    """View para a página inicial do módulo de análises"""
    template_name = 'app/home_analises.html'

class UmidadeCreateView(CreateView):
    model = AnaliseUmidade
    form_class = AnaliseUmidadeForm
    template_name = 'app/cadastro_umidade.html'
    success_url = reverse_lazy('analises:umidade_list')

class ProteinaCreateView(CreateView):
    model = AnaliseProteina
    form_class = AnaliseProteinaForm
    template_name = 'app/cadastro_proteina.html'
    success_url = reverse_lazy('analises:proteina_list')

class OleoDegomadoCreateView(CreateView):
    model = AnaliseUmidadeOleoDegomado
    form_class = AnaliseUmidadeOleoDegomadoForm
    template_name = 'app/cadastro_umidade_oleo.html'
    success_url = reverse_lazy('analises:oleo_list')

class UmidadeListView(ListView):
    model = AnaliseUmidade
    template_name = 'app/lista_umidade.html'

class ProteinaListView(ListView):
    model = AnaliseProteina
    template_name = 'app/lista_proteina.html'

class OleoDegomadoListView(ListView):
    model = AnaliseUmidadeOleoDegomado
    template_name = 'app/lista_umidade_oleo.html'


class AcidezOleoDegomadoCreateView(CreateView):
    model = AnaliseUmidadeOleoDegomado
    form_class = AnaliseUmidadeOleoDegomadoForm
    template_name = 'app/cadastro_oleo_acidez.html'
    success_url = reverse_lazy('analises:acidez_list')


class AcidezOleoDegomadoListView(ListView):
    model = AnaliseUmidadeOleoDegomado
    template_name = 'app/lista_acidez_oleo.html'