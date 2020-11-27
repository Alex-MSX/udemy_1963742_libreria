from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('libros/', views.Lista_Libros.as_view(), name='lista_libros'),
    path('', views.Lista_Autores.as_view(), name='lista_autores'),
    path('autor/<int:pk>/libros/', views.Lista_Libros_Autor.as_view(), name='lista_libros_autor'),
    path('autor/nuevo/', views.Agregar_Autor.as_view(), name='agregar_autor'),
    path('autor/editar/<int:pk>/', views.Editar_Autor.as_view(), name='editar_autor'),
    path('autor/eliminar/<int:pk>/', views.Eliminar_Autor.as_view(), name='eliminar_autor'),
    path('autor/<int:pk>/libro/nuevo/', views.Agregar_Libro.as_view(), name='agregar_libro'),
]
