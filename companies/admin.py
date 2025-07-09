from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'email', 'phone', 'is_active', 'subscription')
    search_fields = ('name', 'cnpj', 'email')
    list_filter = ('is_active',)
    # Use raw_is_fields para o campo subscription também, já que ele é um ForeignKey/OneToOneField
    raw_is_fields = ('subscription',)