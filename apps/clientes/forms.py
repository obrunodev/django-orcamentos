from apps.clientes.models import Cliente
from shared.forms import BaseModelForm


class ClienteForm(BaseModelForm):

    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'possui_whatsapp', 'email', 'endereco']
