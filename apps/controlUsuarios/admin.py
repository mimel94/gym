from django.contrib import admin
from .models import Usuario, Plan, Sucursal, ValoracionMedica
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Plan)
admin.site.register(Sucursal)
admin.site.register(ValoracionMedica)