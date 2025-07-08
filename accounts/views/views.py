from django.contrib.auth.forms import AuthenticationForm as MeuForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.urls import reverse_lazy
from accounts.forms.forms import LoginForm, PreCadastroForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# View que processa o formulário de LOGIN
class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'
    authentication_form = LoginForm
    success_url = reverse_lazy('core:dashboardview')



def pre_cadastro_view(request): # View para o pré-cadastro
    if request.method == 'POST': # Verifica se o método da requisição é POST
        # Se for POST, cria uma instância do formulário com os dados enviados
        form = PreCadastroForm(request.POST)
        if form.is_valid(): # Verifica se o formulário é válido
            form.save() # Salva os dados do formulário no modelo PreCadastro
            
            # Enviar e-mail com os dados do cliente
            dados = form.cleaned_data # Obtém os dados limpos do formulário
            enviar_email_dados_cliente(dados) # Envia o e-mail com os dados do cliente
            
            # Exibir mensagem de sucesso
            messages.success(request, 'Sua solicitação foi enviada com sucesso. Entraremos em contato em breve!')
            return redirect('accounts:precadastroview') # Redireciona para a mesma página após o envio bem-sucedido
        
    # Se o método não for POST, cria um formulário vazio
    else:
        form = PreCadastroForm() # Cria uma instância vazia do formulário PreCadastroForm
    return render(request, 'accounts/cadastro.html', {'form': form}) # Renderiza o template 'accounts/cadastro.html' com o formulário



def enviar_email_dados_cliente(dados): # Função para enviar e-mail com os dados do cliente
    assunto = "Nova Solicitação de Registro no Sistema" # Assunto do e-mail
    remetente = "luancristianrodriguesalves@gmail.com" # Remetente do e-mail
    destinatarios = ["luanalves9895@gmail.com"] # Lista de destinatários do e-mail

    # Contexto para o template do e-mail
    contexto = {
        "nome": dados.get("nome"),
        "email": dados.get("email"),
        "telefone": dados.get("telefone"),
        "empresa": dados.get("empresa"),
        "mensagem": dados.get("mensagem")
    }

    corpo_texto = render_to_string("accounts/emails/solicitacao.txt", contexto) # Corpo do e-mail em texto simples
    corpo_html = render_to_string("accounts/emails/solicitacao.html", contexto) # Corpo do e-mail em HTML

    # Criação do e-mail com o assunto, corpo em texto e HTML, remetente e destinatários
    email = EmailMultiAlternatives(
        subject=assunto,
        body=corpo_texto,
        from_email=remetente,
        to=destinatarios
    )
    
    # Anexa o corpo HTML ao e-mail
    email.attach_alternative(corpo_html, "text/html")
    email.send() # Envia o e-mail
