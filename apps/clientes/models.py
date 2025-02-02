from apps.empresas.models import Empresa
from django.db import models
from shared.models import BaseModel


class Cliente(BaseModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField('Nome completo', max_length=255)
    telefone = models.CharField('Telefone', max_length=16)
    possui_whatsapp = models.BooleanField('Possui Whatsapp?', default=True)
    email = models.EmailField('E-mail', blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.nome
