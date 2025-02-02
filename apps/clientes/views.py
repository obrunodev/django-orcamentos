from apps.clientes.forms import ClienteForm
from apps.clientes.models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy


class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    context_object_name = 'clientes'
    paginate_by = 10


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:list')


class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:list')
