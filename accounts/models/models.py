from django.db import models


# Modelo para pré-cadastro de usuários
# Este modelo é utilizado para armazenar informações de usuários que se inscrevem antes de criar uma conta.
# Ele pode ser usado para coletar informações de contato e interesse antes do registro formal.
class PreCadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Pré-Cadastro'
        verbose_name_plural = 'Pré-Cadastros'
        ordering = ['-criado_em']  # Ordena por data de cadastro, do mais recente para o mais antigo.