from django.contrib.auth.models import User
from django.db import models
from shared.models import BaseModel

class Empresa(BaseModel):
    nome = models.CharField('Nome da empresa', max_length=255)
    cnpj = models.CharField('CNPJ', max_length=20, blank=True, default='')
    endereco = models.CharField('Endereço', max_length=255, blank=True, default='')
    usuarios = models.ManyToManyField(User, blank=True, related_name='empresas')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    
    def __str__(self):
        return self.nome
