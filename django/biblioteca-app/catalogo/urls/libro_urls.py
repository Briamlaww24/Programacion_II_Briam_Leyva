from django.urls import path
from catalogo.views import libro_views

urlpatterns = [
    path('libros/', libro_views.libro_list, name='libro_list'),
    path('libros/crear/', libro_views.create_libro, name='libro_create'),
    path('libros/<int:pk>/editar/', libro_views.update_libro, name='libro_update'),
    path('libros/<int:pk>/eliminar/', libro_views.delete_libro, name='libro_delete'),
]
