
from itertools import tee
from rest_framework import viewsets
from rest_framework import permissions
from api.personal.serializers import EquipoSerializer, JugadoresSerializer, TecnicosSerializer
from personal.models import *


class EquipoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class JugadoresViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Jugadores.objects.all()
    serializer_class = JugadoresSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


class TecnicosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Tecnicos.objects.all()
    serializer_class = TecnicosSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]