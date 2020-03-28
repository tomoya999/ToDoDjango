from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.views import LoginView, LogoutView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'registration/signup.html'

class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'registration/top.html'
