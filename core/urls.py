from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SolicitationViewSet, ImportExcelView

# Registrar as rotas do DefaultRouter
router = DefaultRouter()
router.register(r'solicitations', SolicitationViewSet)  # Adiciona as rotas da API para Solicitation

# Combinar as rotas do router com outras rotas
urlpatterns = router.urls + [
    path('import-excel/', ImportExcelView.as_view(), name='import-excel'),
]
