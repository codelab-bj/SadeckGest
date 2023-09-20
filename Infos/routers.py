from rest_framework.routers import DefaultRouter

from gestion.viewsets import (ContratViewset, ClientViewset,
                              AgenceViewset, MachineViewset)

router = DefaultRouter()

router.register('client', ClientViewset, basename='clients')
router.register('contrat', ContratViewset, basename='contrats')
router.register('agence', AgenceViewset, basename='agences')
router.register('machine', MachineViewset, basename='machines')

urlpatterns = router.urls
