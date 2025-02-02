from apps.clientes.models import Cliente
from django.contrib import admin


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    ...
