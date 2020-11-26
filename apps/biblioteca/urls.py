from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('libros/', views.Lista_Libros.as_view(), name='lista_libros'),
    path('autores/', views.Lista_Autores.as_view(), name='lista_autores'),
    path('libros/<int:pk>', views.Lista_Libros_Autor.as_view(), name='lista_libros_autor'),
]
