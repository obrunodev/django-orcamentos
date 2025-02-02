from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('usuarios/', include('apps.usuarios.urls')),
    path('admin/', admin.site.urls),
    path('clientes/', include('apps.clientes.urls')),
]
