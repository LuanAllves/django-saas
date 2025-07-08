from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from accounts.models.models import PreCadastro
from captcha.fields import CaptchaField # Importando o CaptchaField


# Formulário de login
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'})
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Sua senha'})
    )

# Formulário de pré registro, se utilizado para coletar informações de contato antes do registro formal
class PreCadastroForm(forms.ModelForm):
    nome = forms.CharField(
        label='Nome Completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'})
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Seu e-mail'})
    )
    telefone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu telefone', 'id': 'id_telefone'})
    )
    empresa = forms.CharField(
        label='Empresa',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sua empresa'}),
        required=False
    )
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sua mensagem', 'rows': 3, 'cols': 40}),
        required=False
    )
    # Adicione o campo captcha diretamente aqui, fora da classe Meta
    captcha = CaptchaField()
    
    class Meta:
        model = PreCadastro
        fields = ('nome', 'email', 'telefone', 'empresa', 'mensagem')