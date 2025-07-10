from django import forms
from .models import Product

class ProductForm(forms.ModelForm): # Formulário para criar/editar produtos
    class Meta:# Meta classe para definir o modelo e os campos do formulário
        # Define o modelo que será utilizado pelo formulário
        model = Product
        fields = ['name', 'description', 'sku', 'quantity', 'min_stock_level', 'cost_price', 'sale_price', 'company'] # Campos que serão exibidos no formulário

    def __init__(self, *args, **kwargs): # Inicializa o formulário
        # Aceita o argumento 'company' do CompanyMixin e o remove antes de passar para super().__init__
        self.company = kwargs.pop('company', None) 
        super().__init__(*args, **kwargs) # Chama o construtor da classe pai para inicializar o formulário
        
        if self.company: # Verifica se a empresa foi passada
        # Filtra o queryset de 'company' para incluir apenas a empresa associada ao usuário
            self.fields['company'].queryset = self.fields['company'].queryset.filter(id=self.company.id) # Filtra queryset para a empresa correta
        # Define o valor inicial do campo 'company' para a empresa associada ao usuário
            self.fields['company'].initial = self.company
            self.fields['company'].widget = forms.HiddenInput() # Esconde o campo company do usuário