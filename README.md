# Justificativa:
+ Para esse projeto decidi utilizar o banco in memory.
+ Foram criados 3 endpoints:
  + Consultar o saldo;
  + Efetuar transações entre constras da mesma titularidade;
  + Consultar extrato mostrando as operações realizadas no mês;

# Etapas para instalação

## Requisitos:
 - python 3.9.16

## Crie uma virtualenv utilizando os comandos abaixo:
+ `$ python3.9 -m venv .venv`

## Para ativar o ambiente virtual
+ `source ,venv/bin/activate`

## Dependências do projeto
+ `pip install -r requirements.txt`

## Rodar o projeto
+ `uvicorn app.main:app --reload`

## Documentação - swagger
+ http://127.0.0.1:8000/docs#/