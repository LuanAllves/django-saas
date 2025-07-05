from django.urls import path
from django.contrib.auth import views as auth_views # Para o logout
from .views import views

app_name='accounts'

urlpatterns = [

    # URL que processa a submissão do formulário de LOGIN (POST)
    path('login/', views.LoginView.as_view(), name='loginview'), 
    
    # URL de logout padrão do Djangos
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
]