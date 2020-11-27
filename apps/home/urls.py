from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('index/', views.Index_View.as_view(), name='index'),
]
