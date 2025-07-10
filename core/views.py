from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def HomeView(request):
    return render (request, 'core/index.html')

@login_required
def DashBoard(request):
    # Supondo que você possa obter o slug da empresa do usuário logado
    # ou de alguma outra forma. Exemplo:
    company_slug = request.user.company.slug  # Adapte isso à sua lógica de obtenção do slug

    # Para redirecionar para a lista de produtos da empresa
    product_list_url = reverse('products:product_list', kwargs={'company_slug': company_slug})
    return render (request, 'core/dashboard.html')