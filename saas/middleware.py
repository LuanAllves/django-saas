import re
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from .settings import LOGIN_NOT_REQUIRED


class LoginRequiredMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None, *args, **kwargs):
        self.exceptions = tuple(re.compile(url) for url in LOGIN_NOT_REQUIRED)
        self.get_response = get_response
        super().__init__(get_response, *args, **kwargs)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Sempre permitir URLs isentas
        for url in self.exceptions:
            if url.match(request.path):
                return None

        # Se a URL não é isenta e o usuário não está logado, redirecionar para login
        if not request.user.is_authenticated:
            return redirect('accounts:loginview')

        return None