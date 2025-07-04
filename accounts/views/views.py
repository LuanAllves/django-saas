from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm as MeuForm
from django.contrib import messages
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse_lazy
from accounts.forms.forms import LoginForm

# View que processa o formulário de LOGIN
class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True
