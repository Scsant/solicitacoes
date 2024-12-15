from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Importação necessária para o redirecionamento


urlpatterns = [
    path('', lambda request: redirect('api/', permanent=True)),  # Redireciona para /api/
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Inclui as rotas do app 'core',
    
]
