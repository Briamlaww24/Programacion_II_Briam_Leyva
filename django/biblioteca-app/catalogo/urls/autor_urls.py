from django.urls import path
from catalogo.views import autor_views

urlpatterns = [
    path('autores/', autor_views.autor_list, name='autor_list'),
    path('autores/crear/', autor_views.autor_create, name='autor_create'),
    path('autores/<int:pk>/editar/', autor_views.autor_update, name='autor_update'),
    path('autores/<int:pk>/eliminar/', autor_views.autor_delete, name='autor_delete'),
]
