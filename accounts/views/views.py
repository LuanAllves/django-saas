from django.contrib.auth.forms import AuthenticationForm as MeuForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse_lazy
from accounts.forms.forms import LoginForm, RegisterForm
from django.views.generic.edit import CreateView 
from django.contrib.auth.models import User

# View que processa o formulário de LOGIN
class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('core:dashboardview')

class RegistroView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'accounts/cadastro.html'
    success_url = reverse_lazy('accounts:loginview')