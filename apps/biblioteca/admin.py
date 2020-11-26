from django.contrib import admin
from . import models
# Register your models here.

# Clase para mostrar diferentes campos en el Admin
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre', 'nacionalidad')

class LibroAdmin(admin.ModelAdmin):
    list_filter = ('autor',)

admin.site.register(models.Autor, AutorAdmin)
admin.site.register(models.Libro, LibroAdmin)
