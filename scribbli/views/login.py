from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView as DjangoLoginView


class LoginView(DjangoLoginView):
    template_name = "public/login.html"
    redirect_authenticated_user = True
    next_page = 'my_home'
