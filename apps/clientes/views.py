from apps.clientes.forms import ClienteForm
from apps.clientes.models import Cliente
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    context_object_name = 'clientes'
    paginate_by = 10


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')

    def form_valid(self, form):
        messages.success(self.request, "Cliente criado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar o cliente.")
        return super().form_invalid(form)


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')

    def form_valid(self, form):
        messages.success(self.request, "Cliente atualizado com sucesso!")
        return super().form_valid(form)


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:list')

    def form_valid(self, form):
        messages.success(self.request, "Cliente excluído com sucesso!")
        return super().form_valid(form)
