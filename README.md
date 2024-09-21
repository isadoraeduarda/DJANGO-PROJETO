# Projeto: Agendamento de Pagamentos

## Especificações

Neste projeto iremos construir uma API em DJANGO REST para realizar criar o agendamento de um pagamento, listar todos os agendamentos de pagamento, consultar todos os pagamentos e deletar agendamentos de pagamento

Os campos requeridos para criar o agendamento do pagamento deve ser: 
+ `data_de_pagamento:`Deve possuir o formato YYYY-MM-DD 
+ `permite_recorrencia : `Deve possuir o formatO booleano.
+ `quantidade_recorrencia : `Deve possuir o formato do tipo inteiro.
+ `intervalo_recorrencia : `Deve possuir o formato do tipo inteiro.
+ `status_recorrencia : `Deve possuir o formato do tipo strng..
+ `agencia : `Deve possuir o formato do tipo inteiro.
+ `conta : `Deve possuir o formato do tipo inteiro.
+ `valor_pagamento : `Deve ser em decimal, mas convertido para inteiro no banco de dados.
  
Metodos HTTP: 
+ `POST: agendamentos/:` Consiste em criar o agendamento. 
+ `GET: agendamentos/all/` Consiste em listar todos os agendamentos.
+ `GET:agendamentos/<int:id>/` Consiste em buscar um agendamento por ID
+ `PUT:'agendamentos/update/<int:id>/'` Consiste em modificar um agendamento por ID
+ `DELETE:agendamentos/delete/<int:id>/`Consiste em deletar um agendamento por ID 

## Etapas de desenvolvimento

Projeto testado e executado na versão 3.9 do python.

### Etapa 00: Instalação, Clonando o Repositório, Criando o Ambiente Virtual e Instalando os Requerimentos.

Antes de começar, você vai precisar instalar em sua máquina a seguinte ferramenta: [Python](https://python.org.br), além disto é importante que tenha ter um editor para trabalhar com o código, recomendo que use o: [VSCode](https://code.visualstudio.com/).

Clone o repositório: `git clone git@github.com:isadoraeduarda/agendamento-de-pagamentos.git`

Crie um ambiete virtual: `python -m venv venv`

Ative o ambiente virtual: 

- Windows: `.\venv\Scripts\activate`
- Linux: `source venv/bin/activate`

Instale as dependencias: `pip install -r requirements.txt`      

Acesse a pasta do projeto Django: `cd solucoesweb`

Rode as migrações: `make migrate`

Execute o projeto: `make`
 
## Endpoints API

### Agendamento de Pagamentos

Utilizar o Postman, Insomnia ou CURL para realizar os testes abaixo

Criar agendamento de pagamento: 

```md
      http:
        POST: agendamentos/
    
      {
      "id": <id do agendamento>,
      "data_pagamento": "<data do pagamento>",
      "permite_recorrencia": <booleano>,
      "quantidade_recorrencia": <inteiro>,
      "intervalo_recorrencia": <inteiro>,
      "status_recorrencia": "<status>",
      "agencia": <inteiro>,
      "conta": <inteiro>,
      "valor_pagamento": <valor em inteiro>
    }
    
    Resposta Esperada:
    Código HTTP: 201
```

Exemplo CURL

```sh
curl --request POST \
  --url http://127.0.0.1:8000/api/agendamentos/ \
  --header 'Content-Type: application/json' \
  --data '{
  "data_pagamento": "2026-09-10",
  "permite_recorrencia": true,
  "quantidade_recorrencia": 1,
  "intervalo_recorrencia": 1,
  "status_recorrencia": "pendente",
  "agencia": 10,
  "conta": 20,
  "valor_pagamento": 40
}
'
```

---

Buscar todos os pagamentos agendados:

```md
      http
        GET: agendamentos/all/

    [{
      "id": <id do agendamento>,
      "data_pagamento": "<data do pagamento>",
      "permite_recorrencia": <booleano>,
      "quantidade_recorrencia": <inteiro>,
      "intervalo_recorrencia": <inteiro>,
      "status_recorrencia": "<status>",
      "agencia": <inteiro>,
      "conta": <inteiro>,
      "valor_pagamento": <valor em inteiro>
    }]
```   

Exemplo CURL

```sh
curl --request GET \
  --url http://127.0.0.1:8000/api/agendamentos/all/ \
  --header 'Content-Type: application/json'
```

---

Modificar pagamento por ID

```md
      http
        PUT:'agendamentos/update/<int:id>/

  
    {
      "id": <id do agendamento>,
      "data_pagamento": "<data do pagamento>",
      "permite_recorrencia": <booleano>,
      "quantidade_recorrencia": <inteiro>,
      "intervalo_recorrencia": <inteiro>,
      "status_recorrencia": "<status>",
      "agencia": <inteiro>,
      "conta": <inteiro>,
      "valor_pagamento": <valor em inteiro>
    }
    
    Resposta Esperada:
    Código HTTP: 200
```

Exemplo CURL

```sh
curl --request PUT \
  --url http://127.0.0.1:8000/api/agendamentos/update/2/ \
  --header 'Content-Type: application/json' \
  --data '{
  "data_pagamento": "2024-09-12",
  "permite_recorrencia": true,
  "quantidade_recorrencia": 1,
  "intervalo_recorrencia": 1,
  "status_recorrencia": "concluído",
  "agencia": 10,
  "conta": 20,
  "valor_pagamento": 22.21
}'
```

---

Deletar agendamento de pagamento por ID  

```md
      http
        `DELETE:agendamentos/delete/<int:id>/


      "id": <id do agendamento>,
      "data_pagamento": "<data do pagamento>",
      "permite_recorrencia": <booleano>,
      "quantidade_recorrencia": <inteiro>,
      "intervalo_recorrencia": <inteiro>,
      "status_recorrencia": "<status>",
      "agencia": <inteiro>,
      "conta": <inteiro>,
      "valor_pagamento": <valor em inteiro>
    }
    
      Resposta Esperada:
      Código HTTP: 204 (sem conteúdo)
```

Exemplo CURL

```sh
curl --request DELETE \
  --url http://127.0.0.1:8000/api/agendamentos/delete/4/ 
```

---

## To do: 

- [ ] Melhorar gestão dos arquivos do banco
