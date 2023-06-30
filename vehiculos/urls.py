from rest_framework import routers
from .api import vehiculoViewSet, imagenvehiculoViewSet, caracteristicasViewSet, teamViewSet


router = routers.DefaultRouter()

router.register('api/vehiculos', vehiculoViewSet)
router.register('api/imagenvehiculos', imagenvehiculoViewSet)
router.register('api/caracteristicas', caracteristicasViewSet)
router.register('api/team', teamViewSet)
urlpatterns = router.urls