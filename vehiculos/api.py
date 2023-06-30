from .models import vehiculo, imagenvehiculo, caracteristicas, team
from rest_framework import viewsets, permissions
from .serializers import vehiculoSerializer, imagenvehiculoSerializer, caracteristicasSerializer, teamSerializer

class vehiculoViewSet(viewsets.ModelViewSet):
    queryset = vehiculo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = vehiculoSerializer

class imagenvehiculoViewSet(viewsets.ModelViewSet):
    queryset = imagenvehiculo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = imagenvehiculoSerializer  

class caracteristicasViewSet(viewsets.ModelViewSet):
    queryset = caracteristicas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = caracteristicasSerializer

class teamViewSet(viewsets.ModelViewSet):
    queryset = team.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = teamSerializer
