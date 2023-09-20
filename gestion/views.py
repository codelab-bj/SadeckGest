"""
from rest_framework import mixins
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from .models import Contrat, Client, Agence, Machine
from .serializers import (ContratSerializer, ClientSerializer,
                          AgenceSerializer, MachineSerializer)

from rest_framework import permissions

# Create your views here.


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Vérifier si l'utilisateur est propriétaire de l'objet
        return obj.owner == request.user


class MyContrat(GenericViewSet, mixins.ListModelMixin,
                mixins.CreateModelMixin, mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
                
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer


class MyClient(generics.GenericAPIView, mixins.ListModelMixin,
               mixins.CreateModelMixin, mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MyAgence(generics.GenericAPIView, mixins.ListModelMixin,
               mixins.CreateModelMixin, mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    queryset = Agence.objects.all()
    serializer_class = AgenceSerializer


class MyMachines(generics.GenericAPIView, mixins.ListModelMixin,
                 mixins.CreateModelMixin, mixins.UpdateModelMixin,
                 mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
"""