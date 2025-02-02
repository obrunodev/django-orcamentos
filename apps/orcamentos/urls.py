from apps.orcamentos import views
from django.urls import path

app_name = 'orcamentos'
urlpatterns = [
    path('', views.OrcamentoListView.as_view(), name='list'),
    path('<int:cliente_id>/novo-orcamento/', views.OrcamentoCreateView.as_view(), name='novo_orcamento'),
    path('<int:pk>/', views.OrcamentoDetailView.as_view(), name='detail'),
    path('<int:orcamento_id>/cancel/', views.OrcamentoCancelView.as_view(), name='cancel'),
]
