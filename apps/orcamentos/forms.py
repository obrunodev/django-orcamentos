from apps.orcamentos.models import Orcamento
from shared.forms import BaseModelForm


class OrcamentoForm(BaseModelForm):

    class Meta:
        model = Orcamento
        fields = ['ambiente']