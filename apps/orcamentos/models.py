from apps.clientes.models import Cliente
from django.contrib.auth.models import User
from django.db import models
from shared.models import BaseModel


class Orcamento(BaseModel):
    class StatusChoices(models.TextChoices):
        EM_DESENVOLVIMENTO = 'em_desenvolvimento', 'Em desenvolvimento'
        AGUARDANDO_CLIENTE = 'aguardando_cliente', 'Aguardando cliente'
        APROVADO = 'aprovado', 'Aprovado'
        RECUSADO = 'recusado', 'Recusado'
        CANCELADO = 'cancelado', 'Cancelado'

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ambiente = models.CharField('Ambiente', max_length=255)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.EM_DESENVOLVIMENTO)
    valor_total = models.DecimalField('Valor do projeto', max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'
    
    def __str__(self):
        return f'Orçamento {self.ambiente} = {self.cliente}'
