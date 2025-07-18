from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # Importa as views genéricas do Django
from django.urls import reverse_lazy # Para redirecionar após a exclusão
from django.shortcuts import get_object_or_404, redirect, render # Importa funções auxiliares para renderizar templates e redirecionar
from django.contrib.auth.mixins import LoginRequiredMixin # Para exigir login
from .models import Product # Importa o modelo Product
from companies.models import Company # Importa o modelo Company
from .forms import ProductForm # Importa o formulário ProductForm 
from django.contrib import messages # Para exibir mensagens de sucesso ou erro

# ---------------------------> mixin para garantir multitenância <---------------------------
class CompanyMixin:
    """ 
    Mixin para obter a empresa com base no company_pk na URL.
    Este mixin é usado para garantir que as views tenham acesso à empresa correta e que o usuário logado pertence a ela.
    """
    
    def dispatch(self, request, *args, **kwargs):
        # 1. Obtém a empresa do slug na URL
        self.company = get_object_or_404(Company, slug=self.kwargs['company_slug']) # Obtém a empresa com base no slug fornecido na URL
        
        # 2. Verifica se o usuário está autenticado
        if not request.user.is_authenticated:
            return self.handle_no_permission() 

        # 3. VERIFICAÇÃO DE AUTORIZAÇÃO CRÍTICA (USANDO request.user.company)
        # Se o usuário não for superusuário E a empresa do usuário não for a empresa da URL, nega acesso.
        if not request.user.is_superuser and (not request.user.company or request.user.company != self.company):
            # Se o usuário não tem uma empresa associada OU a empresa associada não é a da URL
            return self.handle_no_permission() 
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        # Garante que as consultas de objetos (Product, etc.) sejam filtradas pela empresa
        return super().get_queryset().filter(company=self.company)
    
    def get_context_data(self, **kwargs):
        # Adiciona a empresa ao contexto para que possa ser usada nos templates
        context = super().get_context_data(**kwargs)
        context['company'] = self.company
        return context
    
    def get_form_kwargs(self):
        # Adiciona a empresa aos kwargs do formulário para que possa ser usada na criação/edição de produtos
        kwargs = super().get_form_kwargs()
        kwargs['company'] = self.company
        return kwargs
    
    def get_success_url(self):
        # Redireciona para a lista de produtos da empresa após sucesso em criação/edição
        return reverse_lazy('products:product_list', kwargs={'company_slug': self.company.slug})
# ---------------------------> Fim do mixin <---------------------------

# ---------------------------> Listagem de Produtos <---------------------------
class ProductListView(LoginRequiredMixin, CompanyMixin, ListView):
    model = Product # Modelo que será utilizado para listar os produtos
    template_name = 'products/product_list.html' # Template que será renderizado
    context_object_name = 'products' # Nome da variável no template que conterá a lista de produtos (products.all())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Obtém o contexto padrão
        context['title_complete'] = 'PRODUTOS CADASTRADOS' # Título da página
        context['add_url'] = reverse_lazy('products:product_create', kwargs={'company_slug': self.company.slug}) # URL para adicionar um novo produto
        context['company'] = self.company # Adiciona a empresa ao contexto
        context['content_title'] = 'PRODUTOS' # Título do conteúdo
        return context
    
# --------------------------------------> Fim da Listagem de Produtos <---------------------------

# ---------------------------> Detalhamento <---------------------------    
class ProductDetailView(LoginRequiredMixin, CompanyMixin, DetailView):
    model = Product # Modelo que será utilizado para detalhar o produto
    template_name = 'products/product_detail.html' # Template que será renderizado
    context_object_name = 'product' # Nome da variável no template que conterá o produto
# --------------------------------------> Fim do Detalhamento <---------------------------

# ---------------------------> Criação <---------------------------
class ProductCreateView(LoginRequiredMixin, CompanyMixin, CreateView):
    model = Product # Modelo que será utilizado para criar o produto
    template_name = 'products/product_form.html' # Template que será renderizado
    form_class = ProductForm # Formulário que será utilizado para criar o produto
    
    def form_valid(self, form):
        # Antes de salvar o formulário, define a empresa correta do produto.
        form.instance.company = self.company
        return super().form_valid(form) # Chama o método da classe base para salvar o formulário e redirecionar
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Obtém o contexto padrão
        context['title_complete'] = 'CADASTRADOS PRODUTOS' # Título da página
        context['content_title'] = 'PRODUTOS' # Título do conteúdo
        context['return_url'] = reverse_lazy('products:product_list', kwargs={'company_slug': self.company.slug}) # URL para retornar à lista de produtos
        return context
# --------------------------------------> Fim da Criação <---------------------------

# ---------------------------> Atualização <---------------------------
class ProductUpdateView(LoginRequiredMixin, CompanyMixin, UpdateView):
    model = Product # Modelo que será utilizado para atualizar o produto
    template_name = 'products/product_form.html' # Template que será renderizado
    form_class = ProductForm # Formulário que será utilizado para atualizar o produto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Obtém o contexto padrão
        context['title_complete'] = 'ATUALIZAR PRODUTO' # Título da página
        context['content_title'] = 'PRODUTOS' # Título do conteúdo
        context['return_url'] = reverse_lazy('products:product_list', kwargs={'company_slug': self.company.slug}) # URL para retornar à lista de produtos
        return context
# ---------------------------------------> Fim da Atualização <---------------------------

# ---------------------------> Exclusão <---------------------------
class ProductDeleteView(LoginRequiredMixin, CompanyMixin, DeleteView):
    model = Product # Modelo que será utilizado para excluir o produto
    template_name = 'products/product_confirm_delete.html' # Template que será renderizado para confirmação de exclusão

    # SOBRESCRITURA PARA EVITAR O ERRO 'company'
    def get_form_kwargs(self):
        # A DeleteView não precisa do argumento 'company' no seu formulário interno.
        # Retornamos apenas os kwargs padrão que a super classe (DeleteView) espera.
        return super(CompanyMixin, self).get_form_kwargs() 
        # Usamos super(CompanyMixin, self) para pular o get_form_kwargs do CompanyMixin
        # e chamar o get_form_kwargs da próxima classe na cadeia de herança (DeleteView)

    # Opcional: Adicionar mensagem de sucesso (requer django.contrib.messages)
    def form_valid(self, form):
        messages.success(self.request, f'Produto "{self.get_object().name}" deletado com sucesso!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # Obtém o contexto padrão
        context['title_complete'] = 'EXCLUIR PRODUTO' # Título da página
        context['content_title'] = 'PRODUTOS' # Título do conteúdo
        context['return_url'] = reverse_lazy('products:product_list', kwargs={'company_slug': self.company.slug}) # URL para retornar à lista de produtos
        return context
# --------------------------------> Fim da Exclusão <---------------------------


"""
Explicação:
- **CompanyMixin**: Este mixin é responsável por garantir que as views tenham acesso à empresa correta e que o usuário logado pertença a ela. Ele obtém a empresa com base no `company_slug` na URL e adiciona a lógica de permissão/autenticação.

- **ProductListView**: Lista todos os produtos da empresa do usuário logado.

- **ProductDetailView**: Exibe os detalhes de um produto específico.

- **ProductCreateView**: Permite a criação de um novo produto, associando-o à empresa do usuário logado.

- **ProductUpdateView**: Permite a atualização de um produto existente, mantendo a associação com a empresa do usuário logado.

- **ProductDeleteView**: Permite a exclusão de um produto, garantindo que o usuário tenha permissão para realizar essa ação.

Essas views utilizam o mixin `CompanyMixin` para garantir que todas as operações sejam realizadas dentro do contexto da empresa correta, garantindo a multitenância do sistema. Além disso, todas as views exigem que o usuário esteja autenticado (`LoginRequiredMixin`), garantindo que apenas usuários logados possam acessar essas funcionalidades.

# Isso é importante para manter a segurança e a integridade dos dados no sistema.
"""

"""
CompanyMixin: Esta é uma Mixin (uma classe que você "mistura" com outras para adicionar funcionalidades) crucial para o multi-tenancy.

dispatch(): É o primeiro método chamado. Ele pega o company_slug da URL, encontra a Company correspondente e a armazena em self.company. Aqui também virá a lógica de segurança (futuramente) para garantir que o usuário logado só acesse os dados de SUA empresa.

get_queryset(): Sobrescreve o método padrão para filtrar automaticamente todos os objetos (Produtos, neste caso) pela company correta. Isso é o cerne do multi-tenancy em consultas.

get_context_data(): Adiciona a instância da Company ao contexto do template, para que você possa usá-la no HTML (ex: mostrar o nome da ótica).

get_form_kwargs(): Passa a company para o formulário.

get_success_url(): Garante que, após uma operação bem-sucedida (criação, edição, exclusão), o usuário seja redirecionado para a lista de produtos daquela mesma empresa.
"""