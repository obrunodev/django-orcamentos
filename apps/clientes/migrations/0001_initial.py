# Generated by Django 4.2.18 on 2025-02-01 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome completo')),
                ('telefone', models.CharField(max_length=16, verbose_name='Telefone')),
                ('possui_whatsapp', models.BooleanField(default=True, verbose_name='Possui Whatsapp?')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('endereco', models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nome'],
            },
        ),
    ]
