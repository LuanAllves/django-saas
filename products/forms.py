from django.utils.translation import gettext_lazy as _ # Importa gettext_lazy para tradução de strings
from django import forms
from .models import Product, Marca, Category

class ProductForm(forms.ModelForm): # Formulário para criar/editar produtos



    class Meta:# Meta classe para definir o modelo e os campos do formulário
        # Define o modelo que será utilizado pelo formulário
        model = Product
        fields = ['description', 'category', 'sku', 'quantity', 'min_stock_level', 'cost_price', 'sale_price', 'company', 'ean', 'reference', 'unit', 'local', 'marca'] # Campos que serão exibidos no formulário
        widgets = {
            'description': forms.Textarea(attrs={'rows': 1, 'cols': 80, 'class': 'descricao'})
        }

    def __init__(self, *args, **kwargs): # Inicializa o formulário
        # Aceita o argumento 'company' do CompanyMixin e o remove antes de passar para super().__init__
        self.company = kwargs.pop('company', None) 
        super().__init__(*args, **kwargs) # Chama o construtor da classe pai para inicializar o formulário
        self.fields['cost_price'].localize = True # Ativa a localização para o campo de preço de custo
        self.fields['sale_price'].localize = True # Ativa a localização para o campo de preço de venda
        
        if self.company: # Verifica se a empresa foi passada
        # Filtra o queryset de 'company' para incluir apenas a empresa associada ao usuário
            self.fields['company'].queryset = self.fields['company'].queryset.filter(id=self.company.id) # Filtra queryset para a empresa correta
        # Define o valor inicial do campo 'company' para a empresa associada ao usuário
            self.fields['company'].initial = self.company
            self.fields['company'].widget = forms.HiddenInput() # Esconde o campo company do usuário

    def clean_sku(self): # Método para validar o campo SKU
        sku = self.cleaned_data.get('sku') # Obtém o valor do campo SKU
        if sku and Product.objects.filter(sku=sku).exists(): # Verifica se já existe um produto com o mesmo SKU
            raise forms.ValidationError("Já existe um produto com este SKU.") # Lança um erro de validação se o SKU já existir
        return sku # Retorna o valor do SKU se não houver erros
    
    def clean_ean(self): # Método para validar o campo EAN
        ean = self.cleaned_data.get('ean') # Obtém o valor do campo EAN
        if ean and Product.objects.filter(ean=ean).exists(): # Verifica se já existe um produto com o mesmo EAN
            raise forms.ValidationError("Já existe um produto com este EAN.") # Lança um erro de validação se o EAN já existir
        return ean # Retorna o valor do EAN se não houver erros
    
    def clean(self): # Método para validar o formulário como um todo
        cleaned_data = super().clean() # Chama o método clean da classe pai para obter os dados limpos
        quantity = cleaned_data.get('quantity') # Obtém o valor do campo quantidade 
        min_stock_level = cleaned_data.get('min_stock_level') # Obtém o valor do campo nível mínimo de estoque
        if quantity is not None and min_stock_level is not None and quantity < min_stock_level: # Verifica se a quantidade é menor que o nível mínimo de estoque
            raise forms.ValidationError("A quantidade não pode ser menor que o nível mínimo de estoque.")   # Lança um erro de validação se a quantidade for menor que o nível mínimo de estoque
        return cleaned_data # Retorna os dados limpos se não houver erros
    

# Formulario de Cadastro de Marca
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']


# Formulario de Cadastro de Marca
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['nome']