from django.urls import path
from django.contrib.auth import views as auth_views # Para o logout
from .views import views

app_name='accounts'

urlpatterns = [

    # URL que processa a submissão do formulário de LOGIN (POST)
    # A view LoginView é uma classe baseada em view que herda de LoginView do Django
    # e usa o formulário LoginForm definido em accounts/forms/forms.py
    path('login/', views.LoginView.as_view(), name='loginview'), 

    # URL que processa a submissão do formulário de REGISTRO (POST)
    # A view RegistroView é uma classe baseada em view que herda de CreateView
    # e usa o formulário RegisterForm definido em accounts/forms/forms.py
    path('register/', views.pre_cadastro_view, name='precadastroview'),
    
    # URL de logout padrão do Djangos
    # A view LogoutView é uma classe baseada em view que herda de LogoutView do Django
    # e processa o logout do usuário
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
]