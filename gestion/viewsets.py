from rest_framework import authentication, permissions, viewsets

from .models import Contrat, Client, Agence, Machine
from .serializers import (ContratSerializer, ClientSerializer,
                          AgenceSerializer, MachineSerializer)


class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ContratViewset(viewsets.ModelViewSet):
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AgenceViewset(viewsets.ModelViewSet):
    queryset = Agence.objects.all()
    serializer_class = AgenceSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MachineViewset(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



