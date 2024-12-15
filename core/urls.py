from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SolicitationViewSet, ImportExcelView
from .views import CMViewSet, PranchasViewSet, TritremViewSet, EscalaDiaViewSet, EscalaNoiteViewSet, ImportInternalView


# Registrar as rotas do DefaultRouter
router = DefaultRouter()
router.register(r'solicitations', SolicitationViewSet)  # Adiciona as rotas da API para Solicitation
router.register(r'cm', CMViewSet, basename='cm')
router.register(r'pranchas', PranchasViewSet, basename='pranchas')
router.register(r'tritrem', TritremViewSet, basename='tritrem')
router.register(r'escala-dia', EscalaDiaViewSet, basename='escala-dia')
router.register(r'escala-noite', EscalaNoiteViewSet, basename='escala-noite')

# Combinar as rotas do router com outras rotas
urlpatterns = router.urls + [
   path('import-excel/', ImportExcelView.as_view(), name='import-excel'),  # Remove o 'api/' extra
   path('import-internal/', ImportInternalView.as_view(), name='import-internal'),
]

