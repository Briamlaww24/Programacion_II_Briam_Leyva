from django.urls import path
from django.contrib.auth.views import LogoutView
from catalogo.views.authentication_views import BibliotecaLoginView

urlpatterns = [
    path('login/', BibliotecaLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
