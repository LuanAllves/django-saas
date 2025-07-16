## Licença

Este projeto está licenciado sob uma Licença Personalizada baseada na MIT, com restrição de uso comercial. Para mais detalhes, veja o arquivo [LICENSE](./LICENSE).


### Guia básico de instalação do sistema Django

# Criando e ativando o ambiente virtual.

## No Windows

> Você pode utilizar o terminal do VSCode para isso, ou abrir um terminal no local do projeto.
>> No terminal digite:
```
>> py -m venv meu_ambiente 
```
>> Obs: "meu_ambiente", pode ser o nome que quiser, mas, por padrão usamos "venv" ou ".venv".

```
>> meu_ambiente/Scripts/Activate 
```
>> Obs: Caso de erro em alguns dos comando, provavelmente está usando o PowerShell ou inves do CMD (Command Prompt), para resolver isso, utilize o CMD ou use o seguindo comando no PowerShell.

```
>> Set-ExecutionPolicy RemoteSigned
```
>> Confirme com "S" quando solicitado.
-------------------------------------------------------------------------------------
> * ### Após a criação e instalação do ambiente virtual, instalamos as dependências:
>> Rode o comando de instalação do requirements:

```
>> pip install -r requirements.txt 
```
-------------------------------------------------------------------------------------
> * ### Depois de instalado, faça as migrações, crie um super usuario e rode o servidor Django:
>> Cria as Migrações:
```
>> python3 manage.py makemigrations
```
>> Migra para o banco de dados.
```
>> py manage.py migrate 
```
>> Crie o SuperUser.
```
>> py manage.py createsuperuser
```
>> Digite o usuario e de enter, o emial (opcional), caso nao queire de enter, e por fim digite a senha e confirme, caso a senha seja fraca, será solicitado uma confirmação.

>> Roda o servidor.
```
>> py manage.py runserver
```

## No MacOS ou Linux

>> No terminal digite:
```
>> python3 -m venv meu_ambiente 
```
>> Obs: "meu_ambiente", pode ser o nome que quiser, mas, por padrão usamos "venv" ou ".venv".

```
>>source meu_ambiente/bin/activate 
```
>> Obs: Se estiver usando o Fish Shell, adicione .fish no final do comando

-------------------------------------------------------------------------------------
> * ### Após a criação e instalação do ambiente virtual, instalamos as dependências:
>> Rode o comando de instalação do requirements:

```
>> pip install -r requirements.txt 
```
-------------------------------------------------------------------------------------
> * ### Depois de instalado, faça as migrações, crie um super usuario e rode o servidor Django:
>> Cria as Migrações:
```
>> python3 manage.py makemigrations
```
>> Migra para o banco de dados.
```
>> py manage.py migrate 
```
>> Crie o SuperUser.
```
>> py manage.py createsuperuser
```
>> Digite o usuario e de enter, o emial (opcional), caso nao queire de enter, e por fim digite a senha e confirme, caso a senha seja fraca, será solicitado uma confirmação.

>> Roda o servidor.
```
>> py manage.py runserver
```