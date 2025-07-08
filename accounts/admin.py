from django.contrib import admin
from .models.models import PreCadastro

@admin.register(PreCadastro)
class SolicitacaodeCadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'empresa', 'telefone', 'criado_em')
    search_fields = ('nome', 'email', 'empresa')
    list_filter = ('criado_em',)
