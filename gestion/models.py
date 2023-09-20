from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS_CHOICES = (
    ('En cour', 'En cour'),
    ('Terminé', 'Terminé'),
)

MACHINE_CHOICES = (
    ('En pause', 'En pause'),
    ('En utilisation', 'En utilisation')
)


class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Contrat(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    duration = models.IntegerField()
    description = models.TextField()
    statu = models.CharField(max_length=15, choices=STATUS_CHOICES)
    debut = models.DateTimeField(auto_now_add=True)
    fin = models.DateField()

    def cost(self):
        return int(self.duration) * 1000

    def __str__(self):
        return f"{self.duration}"


class Agence(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    telephone = models.IntegerField()
    mail = models.EmailField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    contrat = models.ForeignKey(Contrat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.client.name})"


class Machine(models.Model):
    name = models.CharField(max_length=128)
    mtype = models.CharField(max_length=128)
    num = models.IntegerField()
    pre_compt = models.IntegerField(null=True)
    after_compt = models.IntegerField(null=True)
    agence = models.ForeignKey(Agence, on_delete=models.SET_NULL, null=True, related_name="agence_machines")
    statu = models.CharField(max_length=50, choices=MACHINE_CHOICES, default='stats')

    def __str__(self):
        return f"{self.name} ({self.num})"


'''
class commande(models.Model):
    prix = models.IntegerField()

    def totalPrix(self):
        return  self.prix * 1000

    def __str__(self):
        return  self.prix
'''