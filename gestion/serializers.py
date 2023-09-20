from rest_framework import serializers

from .models import Client, Machine, Agence, Contrat


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class ContratSerializer(serializers.ModelSerializer):
    costs = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Contrat
        fields = ('client', 'duration', 'description', 'statu', 'debut', 'fin', 'costs')

    def get_costs(self, obj):
        return obj.cost()


class AgenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agence
        fields = ('name', 'address', 'telephone', 'mail', 'client', 'contrat')


class MachineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Machine
        fields = ('name', 'mtype', 'num', 'statu', 'pre_compt', 'after_compt', 'agence')

