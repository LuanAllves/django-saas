from django.urls import path
from . import views

app_name = 'products' # Define o namespace para as URLs do aplicativo

# Define as URLs do aplicativo products
# Cada URL é mapeada para uma view específica
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'), # Lista todos os produtos.
    path('adicionar/', views.ProductCreateView.as_view(), name='product_create'), # Cria um novo produto.
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'), # Detalhes de um produto específico.
    path('<int:pk>/editar/', views.ProductUpdateView.as_view(), name='product_update'), # Edita um produto específico.
    path('<int:pk>/excluir/', views.ProductDeleteView.as_view(), name='product_delete'), # Deleta um produto específico.
    path('add/marca/', views.MarcaCreateView.as_view(), name='marca_add'), # Cadastrar uma Marca.
    path('add/categoria/', views.CategoryCreateView.as_view(), name='category_add'), # Cadastrar Categoria
]

"""
Explicação:
- `app_name`: Define o namespace para as URLs do aplicativo, permitindo que as URLs sejam referenciadas de forma única em todo o projeto.
- `urlpatterns`: Lista de URLs do aplicativo, onde cada URL é mapeada para uma view específica usando o método `as_view()` das classes de views baseadas em classe do Django.
- Cada URL tem um nome associado, que pode ser usado para referenciar a URL em templates or views, facilitando a manutenção e a legibilidade do código.(exemplo, `product_list`, `product_create`, etc.).
- As views são importadas do módulo `views`, que deve conter as classes correspondentes para cada operação CRUD (Create, Read, Update, Delete) relacionadas aos produtos.
# Isso permite que o Django saiba qual view deve ser chamada quando uma URL específica é acessada.
"""

"""
'<int:pk>/': Este padrão captura um inteiro (geralmente o ID do produto) e o passa como argumento `pk` para a view correspondente.
# Isso é útil para operações que precisam identificar um produto específico, como detalhes, edição ou exclusão.
"""