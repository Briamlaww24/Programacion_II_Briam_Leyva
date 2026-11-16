from django.contrib.auth.views import LoginView


class BibliotecaLoginView(LoginView):
    template_name = 'catalogo/authentication/login.html'
    redirect_authenticated_user = True
