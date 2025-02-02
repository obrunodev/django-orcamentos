from apps.clientes.models import Cliente
from apps.orcamentos.forms import OrcamentoForm
from apps.orcamentos.models import Orcamento
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView


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
            return redirect(reverse('orcamentos:detail', kwargs={'pk': obj.id}))
        context = {
            'cliente': cliente,
            'form': OrcamentoForm,
        }
        return render(request, 'orcamentos/orcamento_form.html', context)


class OrcamentoDetailView(DetailView):
    model = Orcamento


class OrcamentoListView(ListView):
    model = Orcamento
    context_object_name = 'orcamentos'
    paginate_by = 10

    def get_queryset(self):
        empresa = self.request.user.empresas.first()
        clientes = Cliente.objects.filter(empresa=empresa)
        orcamentos = Orcamento.objects.filter(cliente__in=clientes).exclude(
            status=Orcamento.StatusChoices.CANCELADO,
        )
        if q := self.request.GET.get('q'):
            orcamentos = orcamentos.filter(
                Q(cliente__nome__icontains=q) |
                Q(usuario__first_name__icontains=q) |
                Q(usuario__email__icontains=q)
            )
        return orcamentos


class OrcamentoCancelView(View):

    def get(self, request, orcamento_id):
        orcamento = get_object_or_404(Orcamento, id=orcamento_id)
        context = {'orcamento': orcamento}
        return render(request, 'orcamentos/orcamento_confirma_cancelamento.html', context)
    
    def post(self, request, orcamento_id):
        orcamento = get_object_or_404(Orcamento, id=orcamento_id)
        try:
            orcamento.status = orcamento.StatusChoices.CANCELADO
            orcamento.save()
            messages.success(request, 'O orçamento foi cancelado!')
        except Exception as error:
            messages.error(request, f'Algo deu errado com o cancelamento! {error}')
        return redirect('orcamentos:list')
