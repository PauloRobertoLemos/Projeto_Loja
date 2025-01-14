# Projeto_Loja
# Como rodar o projeto

### Instruções de instalação
1. Instalar a versão mais atualizado do python.
2. Instalar a IDE -> VSCode.
3. Instale no terminal do VSCode o crispy_forms pelo comando -> pip install django-crispy-forms e instale o crispy_bootstrap5 pelo comando -> pip install crispy-bootstrap5;

### Instruções de Iniciação
1. Clonar o repositório.
2. Criar um ambiente Virtual.
OBS: Tentei criar com vemv, porem meu computador não conseguiu conectar com o banco de dados local, por causa das portas da placa mãe, que não está funcionando. Então criei sem usar o vemv e consegui conectar com o banco de dados.
     Sei que usar o vemv é diferencial, mais se não fosse o meu computador eu conseguiria usar o vemv.

## Comando para abrir o terminal de maneira mais rápida e fácil
1. Utiliza o comando CTRL + J.

## Comando para transformar os codigos do Python em dados do SQLITE e para migrar os dados para o banco de dados
1. Utilizamos o comando -> python manage.py makemigrations, para transformar as linhas de código em dados.
2. Utilizamos o comando -> python manage.py migrate, para transportar/colocar os dados para o banco de dados.

## Para inciar a aplicação utilize o código abaixo no terminal
1. Utilizamos o comando -> python manage.py runserver, para iniciar a aplicação, depois que o comando for lido aprete CTRL + Botão Esquerdo do mouse no link que foi criado para abir a página no navegador.
