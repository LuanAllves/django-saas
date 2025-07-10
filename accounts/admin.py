from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models.models import PreCadastro, CustomUser

@admin.register(PreCadastro)
class SolicitacaodeCadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'empresa', 'telefone', 'criado_em')
    search_fields = ('nome', 'email', 'empresa')
    list_filter = ('criado_em',)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'company')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'company__name')
    list_filter = ('is_staff', 'is_active', 'company')

    # Fieldsets para o formulário de edição de usuário existente
    fieldsets = UserAdmin.fieldsets + (
        (('Informações da Empresa'), { 'fields': ('company',)}),
    )

    # Fieldsets para o formulário de criação de novo usuário
    add_fieldsets = UserAdmin.add_fieldsets + (
        (('Informações da Empresa'), {'fields': ('company',)}),
    )

    ordering = ('company__name', 'username')  # Ordena os usuários pelo nome da empresa e pelo nome de usuário