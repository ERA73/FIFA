from django.urls import include, path
from rest_framework import routers
from api.personal.views import EquipoViewSet, JugadoresViewSet, TecnicosViewSet, ReporteViewSet

# router = routers.DefaultRouter()
# router.register(r'equipos', EquipoViewSet)
# router.register(r'jugadores', JugadoresViewSet)
# router.register(r'tecnicos', TecnicosViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/equipos/<int:pk>', EquipoViewSet.as_view()),
    path('api/jugadores/<int:pk>', JugadoresViewSet.as_view()),
    path('api/tecnicos/<int:pk>', TecnicosViewSet.as_view()),
    path('api/reporte/', ReporteViewSet.as_view()),
]