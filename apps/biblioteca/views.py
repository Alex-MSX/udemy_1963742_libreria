from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
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
    context_object_name = 'autor'

    def get_queryset(self):
        id = self.kwargs['pk']
        context = models.Autor.objects.get(pk=id)
        return context

class Lista_Libros_Autor1(TemplateView):
    template_name = 'biblioteca/libros-autor.html'
    # context_object_name = 'libros'

    # def get_queryset(self):
    #     context = {}
    #     print(self.kwargs)
    #     id = self.kwargs['pk']
    #     # Para que esto funcione, necesito el parámetro related_name en mi modelo
    #     #context = models.Autor.objects.get(pk=id).libros.all()
    #
    #
    #     context = models.Libro.objects.filter(autor=id)
    #     print(context)
    #     # Cuando deseo filtrar por un parametro de otro modelo pongo model__campo
    #     #context = models.Libro.objects.filter(autor__nacionalidad=id)
    #     #context = models.Autor.objects.get(nacionalidad=id).libros.all()
    #
    #     return context

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        id = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['autor'] = models.Autor.objects.get(pk=id)
        context['libros'] = models.Libro.objects.filter(autor=id)
        return context

class Agregar_Autor(CreateView):
    template_name = 'biblioteca/crear-autor.html'
    model = models.Autor
    fields = ['nombre','nacionalidad']
    success_url = '/'

class Editar_Autor(UpdateView):
    template_name = 'biblioteca/editar-autor.html'
    model = models.Autor
    fields = ['nombre','nacionalidad']
    success_url = '/'

class Eliminar_Autor(DeleteView):
    template_name = 'biblioteca/eliminar-autor.html'
    model = models.Autor
    success_url = '/'

class Agregar_Libro(CreateView):
    template_name = 'biblioteca/agregar-libro.html'
    model = models.Libro
    fields = ['titulo', 'resumen', 'autor']

    def get_success_url(self):
        print(self.kwargs)
        return reverse('biblioteca:lista_libros_autor', kwargs={'pk': self.kwargs['pk']})
