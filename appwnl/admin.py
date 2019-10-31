from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Empresa)
admin.site.register(Desenvolvedor)
admin.site.register(Endereco)
admin.site.register(Tecnologia)
admin.site.register(Reserva)
admin.site.register(Local)

