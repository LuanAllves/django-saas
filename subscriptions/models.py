from django.db import models

# ------------------> Inicio do modelo de Plano <-----------------------------------
# Esse modelo é responsavel por gerenciar os Planos, aqui armazenamos as informações que esses planos tem, como preço, nome, descrição, se esta ativo, lista de recursos e etc.
# Uma relação de um para muitos, ou seja, um unico plano pode pertencer a varios clientes.

class Plan(models.Model):
    """
    Representa um plano de assinatura disponível no sistema.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome do Plano")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço Mensal")
    description = models.TextField(blank=True, verbose_name="Descrição")
    features = models.TextField(blank=True, help_text="Liste os recursos separados por vírgula (ex: '5 usuários, 10GB armazenamento')", verbose_name="Recursos")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Plano"
        verbose_name_plural = "Planos"
    
    def __str__(self):
        return self.name
# ------------------> Fim do modelo de Plano <-----------------------------------

# ------------------> Inicio do modelo Subscription <----------------------------
# Esse modelo é responsavel por gerenciar o Plano ativo do cliente, uma relação de um para um, ou seja, cada cliente só pode ter um plano ativo por vez.
# Com isso conseguimos rastrear o status de cada cliente (ativo, inativo, qual plano usa, quando vence, quais recursos usa).

class Subscription(models.Model):
    """
    Representa a assinatura de uma empresa a um plano específico
    """
    company = models.ForeignKey(
        'companies.Company', # Referencia o modelo de Empresa como uma string, que foi criado anteriormente.
        on_delete=models.CASCADE, # Se a empresa for excluída, todas as assinaturas associadas também serão excluídas.
        related_name='subscriptions', # Permite acessar as assinaturas a partir da empresa (Company.subscriptions).
        verbose_name="Empresa" # Nome do campo na interface administrativa.
    )
    
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name="subscriptions", verbose_name="Plano") # Protege contra exclusão de planos que estão em uso.
    start_date = models.DateField(auto_now_add=True, verbose_name="Data de Início", ) # Data de início da assinatura, padrão é a data atual.
    end_date = models.DateField(null=True, blank=True, verbose_name="Data de Término") # Para assinaturas com peíodo fixo.
    is_active = models.BooleanField(default=True, verbose_name="Ativa") # Indica se a assinatura está ativa ou não.
    auto_renew = models.BooleanField(default=True, verbose_name="Renovação Automática") # Indica se a assinatura será renovada automaticamente.
    last_payment_date = models.DateField(null=True, blank=True, verbose_name="Último Pagamento") # Data do último pagamento, pode ser usada para rastrear quando foi a última cobrança
    next_billing_date = models.DateField(null=True, blank=True, verbose_name="Próxima Cobrança") # Data da próxima cobrança, pode ser usada para rastrear quando será a próxima cobrança
    created_at = models.DateTimeField(auto_now_add=True) # Data de criação da assinatura, padrão é a data atual.
    updated_at = models.DateTimeField(auto_now=True) # Data de atualização da assinatura, atualizada automaticamente sempre que o objeto é salvo.

    class Meta: # Meta class para definir opções adicionais do modelo.
        verbose_name = "Assinatura" # Nome singular do modelo.
        verbose_name_plural = "Assinaturas" # Nome plural do modelo.

        # Adiciona uma restrição única para garantir que um usuário só tenha uma assinatura ativa por vez.
        # Isso é importante para evitar que um usuário tenha múltiplas assinaturas ativas ao mesmo tempo.
        # A condição é que a assinatura deve estar ativa (is_active=True).
        constraints = [ 
            models.UniqueConstraint(fields=['company'], condition=models.Q(is_active=True), name='unique_active_subscription_for_company')
        ]
    
    def __str__(self):
        return f"Assinatura de {self.company.name} - {self.plan.name}"