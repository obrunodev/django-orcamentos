from apps.orcamentos import views
from django.urls import path

app_name = 'orcamentos'
urlpatterns = [
    path('<int:cliente_id>/novo-orcamento/', views.OrcamentoCreateView.as_view(), name='novo_orcamento'),
]
