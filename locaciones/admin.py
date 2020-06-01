from django.contrib import admin

from .models import *

admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Comuna)
admin.site.register(Barrio)
admin.site.register(PuestoVotacion)


