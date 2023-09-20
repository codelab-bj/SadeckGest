from django.contrib import admin

from .models import (Agence, Client, Contrat, Machine)

# Register your models here.
admin.site.register(Contrat)
admin.site.register(Client)
admin.site.register(Machine)
admin.site.register(Agence)


