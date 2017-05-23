# [STHIMA] Avaliação Técnica

## Dependencias
* Python 3.5

## Construindo o ambiente
`pip install -r requirements.txt`

Renomear o arquivo .env.example e adicionar uma SECRET_KEY.

Criar as tabelas do banco de dados:
`./manage migrate`

Executar localmente o servidor:
`./manage runserver`

Acessar a url:
`http://localhost:8000/todo-list/`
