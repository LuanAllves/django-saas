from django.contrib import admin
from .models import Plan, Subscription

# Admin para gerenciar os modelos de assinatura e plano no Django Admin
# Aqui registramos os modelos Plan e Subscription para que possam ser gerenciados através do Django Admin interface.

@admin.register(Plan)
# PlanAdmin é uma classe que herda de admin.ModelAdmin, que é a classe base para personalizar a interface de administração do Django para o modelo Plan.
class PlanAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price', 'is_active', 'created_at', 'update_at') # Exibe os campos principais na lista de planos
    search_fields = ('name', 'description') # Permite buscar pelo nome e descrição do plano
    list_filter = ('is_active',) # Filtros para facilitar a visualização dos planos ativos


@admin.register(Subscription)
# SubscriptionAdmin é uma classe que herda de admin.ModelAdmin, que é a classe base para personalizar a interface de administração do Django para o modelo Subscription.
class SubscriptionAdmin(admin.ModelAdmin): 
    
    list_display = ('company', 'plan', 'start_date', 'end_date', 'is_active', 'next_billing_date') # Exibe os campos principais na lista de assinaturas
    search_fields = ('company__username', 'plan__name') # Permite buscar pelo nome do usuário e do plano
    list_filter = ('is_active', 'plan') # Filtros para facilitar a visualização das assinaturas ativas e planos
    raw_id_fields = ('company', 'plan')  # Permite usar campos de ID bruto para selecionar usuários e planos, melhorando a performance em listas grandes

    # para o que serve raw_id_fields?
    # O raw_id_fields permite que você use um campo de entrada de ID bruto para selecionar objetos relacionados, em vez de um campo de seleção padrão. Isso é útil quando você tem muitos objetos relacionados e deseja evitar a lentidão do carregamento de uma lista suspensa grande. Ele permite que você digite o ID do objeto diretamente ou selecione-o por meio de uma pesquisa rápida.
    # Isso é especialmente útil quando você tem muitos usuários ou planos e deseja evitar a lentidão do carregamento de uma lista suspensa grande. Com raw_id_fields, você pode digitar o ID do usuário ou do plano diretamente ou usar uma pesquisa rápida para encontrá-los, tornando a interface mais responsiva e fácil de usar.