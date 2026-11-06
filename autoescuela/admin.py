from django.contrib import admin
from .models import ClaseManejo

@admin.register(ClaseManejo)
class ClaseManejoAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'categoria_licencia', 'horas_programadas', 'completada')
    search_fields = ('estudiante', 'categoria_licencia')
    list_filter = ('completada', 'categoria_licencia')