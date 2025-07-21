from django.db import models

# Defina as opções de unidade de medida
UNIT_CHOICES = [
    ('UN', 'Unidade(s)'),
    ('CX', 'Caixa(s)'),
    ('PCT', 'Pacote(s)'),
    ('PÇ', 'Peça(s)'),
    ('KG', 'Quilograma(s)'),
    ('LT', 'Litro(s)'),
    ('MT', 'Metro(s)'),
    ('DZ', 'Dúzia(s)'),
    # Adicione mais unidades conforme necessário
]

# Definir as opções de Categoria
CATEGORY_CHOICES = [
    ('Lente', 'Lente'),
    ('Óculos', 'Óculos'),
    ('Armação', 'Armação'),
    ('Acessórios', 'Acessório'),
    ('Equipamentos', 'Equipamento')

]

# Aqui Criamos um modelo de Marca para que os Usuários consiga cadastrar uma nova Marca caso não exista no sistema.
class Marca(models.Model):
    nome = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.nome = self.nome.strip().capitalize()  # ou title() se quiser capitalizar todas as palavras
        super().save(*args, **kwargs)


# Aqui Criamos um modelo de Categoria para que os Usuários consiga cadastrar uma nova Marca caso não exista no sistema.
class Category(models.Model):
    nome = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.nome = self.nome.strip().capitalize()  # ou title() se quiser capitalizar todas as palavras
        super().save(*args, **kwargs)


# Modelo de produto.
class Product(models.Model):
    description = models.TextField(verbose_name='Descrição', blank=True, null=True, help_text="Descrição do produto")
    cost_price = models.DecimalField(verbose_name='Custo', max_digits=10, decimal_places=2, blank=True, null=True, help_text="Preço de custo do produto")
    sale_price = models.DecimalField(verbose_name='Venda', max_digits=10, decimal_places=2, blank=True, null=True, help_text="Preço de venda do produto")
    created_at = models.DateTimeField(verbose_name='Criação', auto_now_add=True, blank=True, null=True, help_text="Data de criação do produto")
    updated_at = models.DateTimeField(verbose_name='Atualização', auto_now=True, blank=True, null=True, help_text="Data de atualização do produto")
    marca = models.ForeignKey(Marca, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(verbose_name='Estoque', default=0, help_text="Quantidade atual em estoque")
    sku = models.CharField(verbose_name='SKU', max_length=20, unique=True, blank=True, null=True, help_text="Código SKU do produto")
    min_stock_level = models.PositiveIntegerField(verbose_name='Min. Estoque', default=0, help_text="Quantidade mínima em estoque para alertas")
    ean = models.CharField(verbose_name='EAN', max_length=13, unique=True, blank=True, null=True, help_text="Código EAN do produto")
    unit = models.CharField(verbose_name='Unidade de Medida', max_length=3, default='UN', choices=UNIT_CHOICES, help_text="Unidade de medida do produto")
    reference = models.CharField(verbose_name='Referência', max_length=20, blank=True, null=True, help_text="Referência do produto")
    local = models.CharField(verbose_name='Local', max_length=20, blank=True, null=True, help_text="Localização do produto no estoque")
    
    
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        related_name='products'
    )
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['-created_at']

