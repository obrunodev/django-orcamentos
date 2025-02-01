from shared.models import BaseModel
from django.db import models


class Cliente(BaseModel):
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
