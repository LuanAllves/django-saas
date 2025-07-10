from django.db import models

# Modelo que representa uma empresa (ótica) no sistema.
# Cada empresa terá uma assinatura associada, que define o plano e as funcionalidades disponíveis.
# ------------------> Modelo Empresa <------------------
class Company(models.Model):
    """
    Representa uma Ótica (cliente) no sistema.
    """

    name = models.CharField(max_length=255, verbose_name="Razão Social") # Nome da empresa
    fantasy_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nome Fantasia") # Nome fantasia da empresa
    cnpj = models.CharField(max_length=18, unique=True, verbose_name="CNPJ") # CNPJ da empresa
    email = models.EmailField(unique=True, verbose_name="E-mail de Contato") # E-mail da empresa
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefone") # Telefone da empresa

    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Endereço") # Endereço da empresa
    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade") # Cidade da empresa
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="Estado") # Estado da empresa
    zip_code = models.CharField(max_length=10, blank=True, null=True, verbose_name="CEP") # CEP da empresa

    is_active = models.BooleanField(default=True, verbose_name="Ativa") # Indica se a empresa está ativa
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug") # Slug para URL amigável da empresa

    # Cada empresa terá uma assinatura.
    # Usaremos OnetoOneField para garantir que uma empresa tenha APENAS UMA assinatura ativa.
    # 'null=True' e 'blank=True' são importantes para a fase de criação, caso a assinatura seja associada após a criação inicial da empresa.

    subscription = models.OneToOneField(
        'subscriptions.Subscription', # Relaciona a assinatura com a empresa como um campo de chave estrangeira.
        related_name='companies', # Nome relacionado para acessar a empresa a partir da assinatura.
        on_delete=models.SET_NULL, # Se a assinatura for excluída, a empresa não será excluída, mas perderá a associação com a assinatura.
        null=True, # Permite que a assinatura seja nula inicialmente
        blank=True, # Permite que a assinatura seja opcional inicialmente
        verbose_name="Assinatura Ativa", # Nome do campo na interface administrativa
    )

    created_at = models.DateTimeField(auto_now_add=True) # Data de criação da empresa
    updated_at = models.DateTimeField(auto_now=True) # Data da última atualização da empresa

    class Meta: # Metadados do modelo
        verbose_name = "Empresa" # Nome singular do modelo na interface administrativa
        verbose_name_plural = "Empresas" # Nome plural do modelo na interface administrativa
        ordering = ["name"] # Ordena as empresas pelo nome por padrão

    def __str__(self): # Método para representar a empresa como string
        return self.name # Retorna o nome da empresa como representação textual
    
# ------------------> Fim do modelo Empresa <------------------