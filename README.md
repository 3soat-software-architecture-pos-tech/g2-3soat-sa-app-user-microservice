# User Microservice

Este é um microserviço de usuários (Customers) construído com Python e Serverless Framework. Ele fornece operações CRUD (Create, Read, Update, Delete) para manipulação de usuários, com persistência de dados no DynamoDB.

![Captura de tela 2024-05-20 231250](https://github.com/3soat-software-architecture-pos-tech/g2-3soat-sa-app-user-microservice/assets/27281151/ec17e5b4-0a68-410e-865a-ace82b99862c)


## Descrição do Projeto

Este projeto consiste em um microserviço para gerenciamento de usuários. Ele fornece endpoints para adicionar, atualizar, buscar e excluir usuários. Os dados dos usuários são armazenados no DynamoDB.

- **core/**: Contém a lógica central do aplicativo, incluindo entidades e casos de uso.
- **infrastructure/**: Contém a lógica de infraestrutura, como a implementação do repositório.
- **api/**: Contém os manipuladores (handlers) da API RESTful, divididos por função.
    - **add_customer/**: Manipulador para adicionar um novo usuário.
    - **delete_customer/**: Manipulador para excluir um usuário existente.
    - **find_all_customers/**: Manipulador para buscar todos os usuários.
    - **find_customer_by_cpf/**: Manipulador para buscar um usuário por CPF.
    - **find_customer_by_id/**: Manipulador para buscar um usuário por ID.
    - **update_customer/**: Manipulador para atualizar os dados de um usuário.
- **tests/**: Contém os testes unitários para garantir a integridade do código.
- **serverless.yml**: Arquivo de configuração do Serverless Framework para definir a infraestrutura e os recursos AWS.
- **requirements.txt**:

## Testes Unitários

Para executar os testes unitários, siga estas etapas:

1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale as dependências listadas no arquivo `requirements.txt` usando o seguinte comando:
    ```bash
    pip install -r requirements.txt
    ```
3. Navegue até o diretório raiz do projeto.
4. Execute o comando abaixo para iniciar os testes:
    ```bash
    pytest
    ```
   Isso executará todos os testes unitários no diretório `tests/` e fornecerá uma cobertura de código.

### Implantação

Para implantar o projeto na AWS usando o Serverless Framework e Docker, siga estas etapas:

1. Certifique-se de ter o Docker instalado em seu sistema.
2. Configure suas credenciais da AWS no GitHub Secrets como `AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY`.
3. Certifique-se de ter o Serverless Framework instalado.

```shell
sls deploy
```

## Materias de Referência
- Alura: [Node js testes unitários e de integração](https://cursos.alura.com.br/course/nodejs-testes-unitarios-integracao)
- Alura: [Node js API Rest com Express e MongoDB](https://cursos.alura.com.br/course/nodejs-api-rest-express-mongodb)
- Alura: [O que é Behavior-Driven Development (BDD)](https://cursos.alura.com.br/extra/alura-mais/o-que-e-behavior-driven-development-bdd--c284)
- Jest: [Documentation](https://jestjs.io/)
- ESLint : [Documentation](https://pt-br.eslint.org/)
- Sonar Cloud: [Documentation](https://docs.sonarsource.com/sonarcloud/)

## Team
 - Turma: 3SOAT
 - Grupo: 2

   [André Felipe](andrefelipegodoi@gmail.com)
   
   [Bruna Carlota](brunacarlota@gmail.com)

   [Carlos Tofoli](henrique.tofoli@hotmail.com)

   [Guilherme Oliveira](guilherme.oliveira182@yahoo.com.br)

   [Valdeir Jesus](valdeir_014@hotmail.com)