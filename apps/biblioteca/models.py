from django.db import models

# Create your models here.

class Autor(models.Model):
    # Clase para poner el plural en los modelos del Admin
    class Meta:
        verbose_name_plural = "Autores"

    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    resumen = models.TextField(blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')

    def __str__(self):
        return self.titulo
