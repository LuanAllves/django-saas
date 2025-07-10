from django.db import models
from django.contrib.auth.models import AbstractUser
from companies.models import Company # Importe o modelo Company


# Modelo para pré-cadastro de usuários
# Este modelo é utilizado para armazenar informações de usuários que se inscrevem antes de criar uma conta.
# Ele pode ser usado para coletar informações de contato e interesse antes do registro formal.
class PreCadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Pré-Cadastro'
        verbose_name_plural = 'Pré-Cadastros'
        ordering = ['-criado_em']  # Ordena por data de cadastro, do mais recente para o mais antigo.

# Modelo de usuário personalizado que herda de AbstractUser
# Este modelo é utilizado para estender as funcionalidades do modelo de usuário padrão do Django.
class CustomUser(AbstractUser):
    """
    Modelo de usuário personalizado que herda de AbstractUser.
    Adiciona um campo para associar o usuário a uma empresa.
    """
    # Campo para armazenar o cargo do usuário.
    # Este campo é opcional, pois pode haver usuários que não possuem um cargo definido.
    cargo = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        verbose_name="Cargo"
    )
    # Campo para associar o usuário a uma empresa.
    # O campo é opcional, pois pode haver usuários que não estão associados a nenhuma empresa
    company = models.ForeignKey(
        Company, 
        on_delete=models.SET_NULL, 
        related_name='users', 
        verbose_name="Empresa Associada",
        null=True, 
        blank=True,
    )

    def __str__(self):
        return self.username or self.email or "Usuário Sem Nome" # Retorna o nome de usuário, email ou uma string padrão se ambos forem vazios.

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']  # Ordena os usuários pelo nome de usuário.