from django.urls import path
from catalogo.views import categoria_views

urlpatterns = [
    path('categorias/', categoria_views.categoria_list, name='categoria_list'),
    path('categorias/crear/', categoria_views.categoria_create, name='categoria_create'),
    path('categorias/<int:pk>/eliminar/', categoria_views.categoria_delete, name='categoria_delete'),
    path('categorias/<int:pk>/editar/', categoria_views.categoria_update, name='categoria_update'),
]
