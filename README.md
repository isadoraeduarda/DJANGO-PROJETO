<h2 align="center"> AGENDAMENTO DE PAGAMENTOS </h2>
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

<h2 align="center"> ETAPAS DE DESENVOLVIMENTO </h2>
<details><summary><strong><h4>Etapa 00: Instalação, Clonando o Repositório, Criando o Ambiente Virtual e Instalando os Requerimentos.</strong></h4></summary>

  
  Antes de começar, você vai precisar instalar em sua máquina a seguinte ferramenta: [Python](https://python.org.br), além disto é importante que tenha ter um editor para trabalhar com o código, recomendamos o: [VSCode](https://code.visualstudio.com/).

  + Clonando o Repositório.
    
      No seu VSCode, será preciso dar o seguinte comando:
   
         git@github.com:isadoraeduarda/agendamento-de-pagamentos.git
  
  + Criando um ambiente virtual:
    
      Windows: 
       
         $ python -m venv venv 
         
      Linux: 
      
        $ python3.9 -m venv venv
        
  + Ativando o ambiente virtual:

     Windows:
     
        $ .\venv\Scripts\activate     
        
     Linux: 
     
        $ source venv/bin/activate
        
  + Instalando os Requerimentos: 

        $ pip install -r requirements.txt
    
+ Para executar o projeto, deve-se: 

     Acessar a camada soluçõesweb, o qual contém os arquivos relacionados a aplicação: 
     
        $ cd solucoesweb
  Após acessar, dar o seguinte comando, isso fará com que o servidor seja rodado: 
     
        make run
 </details>

<details><summary><h4>Etapa 01: Endpoints APIs. </h4></summary>

  <h3 align="center"> AGENDAMENTO DE PAGAMENTOS </h3>

  Utilizar o Postman, Insomnia ou CURL  para realizar os testes abaixo

  + Retorna todos os usuários: 

      http
        GET /api/users



  + Criar agendamento de pagamento:

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




  + Buscar todos os pagamentos agendados:

      http
        GET: agendamentos/all/

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
    
    
    

  + Modificar pagamento por ID

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


  + Deletar agendamento de pagamento por ID  

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

</details>

<h2 align="center"> CRIADORA </h2>

<a href="https://www.linkedin.com/in/isadora-eduarda/" target="_blank_"><img height="25cm"
src="https://img.shields.io/badge/ISADORA-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>




