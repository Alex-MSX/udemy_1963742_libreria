from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class Lista_Libros(ListView):
    template_name = 'biblioteca/libros.html'
    model = models.Libro
    # queryset = models.Libro.objects.all()
    context_object_name = 'libros'

class Lista_Autores(ListView):
    template_name = 'biblioteca/autores.html'
    model = models.Autor
    context_object_name = 'autores'

class Lista_Libros_Autor(ListView):
    template_name = 'biblioteca/libros-autor.html'
    context_object_name = 'libros'

    def get_queryset(self):
        print(self.kwargs)
        id = self.kwargs['pk']
        # Para que esto funcione, necesito el parámetro related_name en mi modelo
        #context = models.Autor.objects.get(pk=id).libros.all()

        context = models.Libro.objects.filter(autor=id)

        # Cuando deseo filtrar por un parametro de otro modelo pongo model__campo
        #context = models.Libro.objects.filter(autor__nacionalidad=id)
        #context = models.Autor.objects.get(nacionalidad=id).libros.all()

        return context
