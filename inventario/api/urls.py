from rest_framework.routers import DefaultRouter
from inventario.api.views import ProductoViewSet

# Definir el router instanciándolo

router = DefaultRouter()

# Registramos la ruta
router.register('productos', ProductoViewSet, basename='producto')
urlpatterns = router.urls # Ahora hay que dirigirnos al urls.py principal del proyecto

