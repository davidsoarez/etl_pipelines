# Projeto ETL com Python, Docker e PostgreSQL

Este projeto é uma pipeline de ETL (Extract, Transform, Load) desenvolvida em Python, utilizando Docker e PostgreSQL. O objetivo é processar dados de um arquivo e carregá-los em uma base de dados PostgreSQL.

## Funcionalidade

O projeto realiza as seguintes etapas:
1. **Extração**: O projeto lê dados de um arquivo localizado na pasta `row`.
2. **Transformação**: Os dados são processados para garantir sua validade e integridade.
3. **Carga**: Os dados transformados são carregados em um banco de dados PostgreSQL.

Após a execução da pipeline, um arquivo contendo apenas os dados válidos é gerado.

## Instruções de Uso

Para iniciar o projeto e executar a pipeline de ETL, siga os passos abaixo:

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/davidsoarez/etl_pipelines.git

Execute o Docker Compose

2. **Execute o comando abaixo para construir e iniciar os containers Docker:**

   ```bash
   docker-compose up --build

Esse comando irá construir a imagem Docker e iniciar os containers necessários para o projeto, incluindo o container do PostgreSQL e o container da aplicação ETL.

## Processamento dos Dados

O arquivo localizado na pasta row será processado automaticamente. Após a conclusão do processo de ETL, um arquivo contendo apenas os dados válidos será gerado.

## Acesso ao PostgreSQL
Para consultar os dados e as informações geradas na base de dados, acesse o container do pgAdmin com as seguintes credenciais:

Usuário: admin@example.com
Senha: admin
Você pode acessar o pgAdmin através do seu navegador na URL http://localhost:5050/login?next=/.

## Observações
Certifique-se de que o Docker e o Docker Compose estão instalados e funcionando corretamente em sua máquina.
Os arquivos de configuração do Docker e do PostgreSQL estão localizados na raiz do projeto.