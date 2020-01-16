from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
from django.shortcuts import redirect
from django.views.generic import CreateView

from authenicate.forms import RegisterForm
from authenicate.models import User


class Login(LoginView):
    http_method_names = ['get', 'post']
    redirect_authenticated_user = True
    template_name = 'authenticate/login.html'


class Logout(LogoutView):
    http_method_names = ['get']
    template_name = 'authenticate/logout.html'

    def get(self, *args, **kwargs):
        super().get(*args, **kwargs)
        return redirect('list')


class Register(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'authenticate/register.html'
    success_url = '/'
