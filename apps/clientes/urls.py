from apps.clientes import views
from django.urls import path

app_name = 'clientes'
urlpatterns = [
    path('', views.ClienteListView.as_view(), name='list'),
    path('create/', views.ClienteCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.ClienteUpdateView.as_view(), name='update'),
    path('<int:pk>/detail/', views.ClienteDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='delete'),
]
