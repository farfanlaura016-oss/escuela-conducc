from django.db import models

class ClaseManejo(models.Model):
    estudiante = models.CharField(max_length=150, verbose_name="Nombre del Estudiante")
    categoria_licencia = models.CharField(max_length=10, verbose_name="Categoría de Licencia")
    horas_programadas = models.IntegerField(verbose_name="Horas Programadas")
    completada = models.BooleanField(default=False, verbose_name="¿Completada?")

    class Meta:
        verbose_name = "Clase de Manejo"
        verbose_name_plural = "Clases de Manejo"
        ordering = ['-id']  # Ordenados del más reciente al más antiguo

    def __str__(self):
        return f"{self.estudiante} - Categoría {self.categoria_licencia}"