from apps.clientes.models import Cliente
from apps.orcamentos.forms import OrcamentoForm
from apps.orcamentos.models import Orcamento
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View


class OrcamentoCreateView(LoginRequiredMixin, View):

    def get(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, id=cliente_id)
        context = {
            'cliente': cliente,
            'form': OrcamentoForm,
        }
        return render(request, 'orcamentos/orcamento_form.html', context)
    
    def post(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, id=cliente_id)
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            obj.cliente = cliente
            obj.save()
            messages.success(request, 'Orçamento gerado!')
            return redirect(reverse('clientes:list'))
        context = {
            'cliente': cliente,
            'form': OrcamentoForm,
        }
        return render(request, 'orcamentos/orcamento_form.html', context)
