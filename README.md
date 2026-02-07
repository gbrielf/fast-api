# FastAPI

## Introdução

FastAPI é um framework Python moderno e de alto desempenho para construção de APIs, criado por Sebastián Ramírez e lançado oficialmente em dezembro de 2018. Ele surgiu para atender a necessidade de criar APIs web rápidas, eficientes e com validação automática de dados, aproveitando recursos modernos do Python 3.6+ como type hints e async/await.

O framework foi projetado para ser intuitivo, rápido de desenvolver e entregar performance comparável a frameworks Node.js e Go, tornando-se uma escolha popular para desenvolvimento de microserviços, aplicações cloud-native e APIs RESTful de alta performance.

No site oficial, o framework é apresentado como um framework "moderno, rápido (alta performance) para construção de APIs com Python 3.8+ baseado em type hints do Python".

## Fundamentos e Arquitetura

### Principais Características

FastAPI é construído sobre Starlette (para partes web) e Pydantic (para validação de dados), oferecendo performance excepcional, comparável a NodeJS e Go. Uma das características mais marcantes é a geração automática de documentação interativa da API (Swagger UI e ReDoc) diretamente a partir do código, facilitando testes e integração.

O uso de type hints do Python permite validação automática de dados, serialização/deserialização, além de fornecer autocompletar e verificação de tipos em editores modernos como VSCode e PyCharm. O framework suporta totalmente programação assíncrona (async/await), permitindo alta concorrência e performance em operações I/O bound.

Adotando padrões modernos de desenvolvimento de APIs, como OpenAPI (anteriormente Swagger) e JSON Schema, FastAPI facilita a integração com outras ferramentas e serviços do ecossistema, sendo flexível e extensível para diferentes estilos de arquitetura.

### Arquitetura Interna

O núcleo do FastAPI utiliza Starlette para funcionalidades ASGI (Asynchronous Server Gateway Interface), fornecendo roteamento, middleware e WebSockets. O Pydantic é responsável pela validação de dados em tempo de execução, conversão de tipos e serialização. A documentação automática é gerada através das especificações OpenAPI e JSON Schema extraídas dos type hints.

### Arquitetura em Camadas

A arquitetura do serviço em FastAPI segue uma organização em camadas que separa responsabilidades e facilita a manutenção do código. Essa estrutura é inspirada em padrões arquiteturais amplamente utilizados em aplicações web modernas.

A aplicação está dividida em camadas bem definidas que trabalham conjuntamente para processar requisições de forma organizada e eficiente:

#### Routers: Camada de Entrada

A camada de **Routers** define os endpoints da API, utilizando decoradores como `@app.get()`, `@app.post()`, etc. Ela é responsável por receber requisições HTTP dos clientes, processar parâmetros de query, path e body, chamar os serviços apropriados e retornar respostas com códigos de status HTTP adequados. Os Routers recebem **modelos Pydantic de entrada**, validam dados automaticamente e delegam a lógica de negócio aos serviços.

#### Services: Lógica de Negócio

A camada de **Services** concentra toda a lógica de negócio da aplicação. Os serviços orquestram chamadas aos repositórios, aplicam validações customizadas, transformam dados e executam as regras do domínio. Dessa forma, a camada de Routers permanece "magra", apenas delegando o processamento aos serviços, que são facilmente testáveis e reusáveis.

#### Models: Modelo de Negócio

A camada de **Models** representa o coração da aplicação, contendo os **modelos de dados** (usando Pydantic ou ORM) e objetos que modelam os conceitos principais do negócio. Esses modelos refletem diretamente as regras e conceitos do domínio (por exemplo, usuários, produtos, pedidos em um sistema de e-commerce). Os modelos são utilizados tanto pelos serviços quanto pelos repositórios.

#### Repositories: Acesso a Dados

A camada de **Repositories** encapsula todo o acesso ao banco de dados, utilizando ORMs como SQLAlchemy ou outros drivers de banco de dados. Os repositórios fornecem métodos para buscar, salvar, atualizar e remover entidades, mantendo a lógica de acesso a dados isolada. Os serviços consomem os repositórios sem precisar conhecer detalhes de SQL ou da tecnologia de persistência utilizada.

#### Schemas: Transferência de Dados

**Schemas** são modelos Pydantic utilizados para validar e serializar dados que trafegam entre a API e o mundo externo. Eles definem a estrutura esperada de requests e responses, fornecendo validação automática, conversão de tipos e geração de documentação. Os schemas evitam expor diretamente os modelos de banco de dados, proporcionando mais segurança e flexibilidade na evolução da API.

## Princípios RESTful com FastAPI

- Design orientado a recursos, com cada endpoint representando um recurso do sistema, manipulado por métodos HTTP (GET, POST, PUT, DELETE, PATCH).
- Uso correto e semântico dos status HTTP para representar os resultados das operações (200, 201, 404, 422, 500, etc.).
- Serialização e deserialização automáticas em JSON através do Pydantic, com suporte a tipos complexos e validações customizadas.
- Validação automática de dados de entrada e documentação interativa gerada automaticamente, facilitando o desenvolvimento e consumo das APIs.
- Suporte a versionamento, autenticação, autorização e outras práticas RESTful modernas.

## Ecossistema e Extensões

FastAPI possui um rico ecossistema de bibliotecas e integrações que complementam suas funcionalidades. Algumas das principais integrações incluem:

- **Persistência**: SQLAlchemy (ORM), Tortoise ORM, MongoDB Motor, PostgreSQL asyncpg, Databases
- **Segurança**: OAuth2, JWT, Python-Jose, Passlib para hashing de senhas
- **Validação**: Pydantic (nativo), Email-validator
- **Testes**: Pytest, HTTPX (cliente assíncrono)
- **Mensageria**: Celery, RabbitMQ, Kafka
- **Observabilidade**: Prometheus, OpenTelemetry, logging estruturado
- **Deployment**: Uvicorn, Gunicorn, Docker, Kubernetes

Bibliotecas são facilmente instaladas via pip, adequando o projeto às necessidades específicas sem adicionar dependências desnecessárias.

## Comparativo com Outros Frameworks

| Framework     | Inicialização          | Consumo de Memória   | Performance         | Validação de Dados     | Documentação Auto | Curva de aprendizado |
|---------------|------------------------|----------------------|---------------------|------------------------|-------------------|----------------------|
| FastAPI       | Muito rápida           | Baixo a moderado     | Muito alta          | Automática (Pydantic)  | Sim (OpenAPI)     | Moderada             |
| Flask         | Rápida                 | Baixo                | Moderada            | Manual                 | Manual            | Simples              |
| Django REST   | Mais lenta             | Alto                 | Moderada            | Manual (Serializers)   | Manual            | Complexa             |

### Detalhes

- **FastAPI** destaca-se pela performance comparável a frameworks em Go e Node.js, validação automática de dados via Pydantic, geração automática de documentação OpenAPI/Swagger, e suporte nativo a async/await.
- **Flask** é minimalista e flexível, ideal para projetos menores ou quando se deseja controle total sobre a arquitetura, porém requer configuração manual de validação e documentação.
- **Django REST Framework** oferece um ecossistema completo e maduro com ORM embutido, admin interface e muitas funcionalidades prontas, mas com overhead maior e performance inferior para APIs puras.

Essa tabela foi construída com base em análises e benchmarks detalhados encontrados em:
- https://www.techempower.com/benchmarks/
- https://fastapi.tiangolo.com/alternatives/
- https://www.digitalocean.com/community/tutorials/fastapi-vs-flask

## Melhores Práticas com FastAPI

Configure routers modulares para organizar endpoints relacionados. Utilize dependency injection do FastAPI para gerenciar conexões de banco de dados, autenticação e outras dependências compartilhadas. Implemente tratamento global de exceções usando exception handlers customizados, sempre padronizando respostas de erro.

Separe modelos Pydantic (schemas) dos modelos ORM para manter flexibilidade na evolução da API. Use variáveis de ambiente e arquivos de configuração para gerenciar diferentes ambientes (dev, staging, prod). Para testes, utilize pytest com TestClient do FastAPI, permitindo testes síncronos de código assíncrono.

A documentação oficial é extremamente completa e didática, sendo um excelente ponto de partida para aprender de forma incremental, com tutoriais passo a passo e exemplos práticos.

## Exemplo Simples: Começando com FastAPI

Este exemplo mostra como criar e executar uma aplicação simples usando FastAPI, seguindo os passos básicos para começar desenvolvendo uma API RESTful.

### Passo 1: Instalação do Python e Pip

FastAPI requer Python 3.8 ou superior. Verifique se o Python está instalado:
```bash
python --version
```

### Passo 2: Instalar FastAPI e Uvicorn

Instale o FastAPI e o servidor ASGI Uvicorn:
```bash
pip install fastapi uvicorn[standard]
```

### Passo 3: Criar o Arquivo da Aplicação

Crie um arquivo `main.py` com o seguinte conteúdo:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

### Passo 4: Executar a Aplicação

Para rodar a aplicação em modo desenvolvimento com hot reload:
```bash
uvicorn main:app --reload
```

Sua aplicação FastAPI estará rodando localmente em:
```
http://localhost:8000
```

A documentação interativa automática estará disponível em:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Passo 5: Hot Reload

Edite o arquivo `main.py` para modificar o texto retornado pelo endpoint.

Altere a mensagem `"Hello World"` para, por exemplo, `"Seminário FastAPI"`. Salve a modificação e atualize seu navegador para ver a mudança refletida instantaneamente, sem precisar reiniciar o servidor (graças ao flag `--reload`).

---

Esse fluxo simples está presente no site oficial do [FastAPI](https://fastapi.tiangolo.com/) e demonstra a rapidez e a facilidade de desenvolvimento com FastAPI, especialmente seu suporte a hot reload e documentação automática para desenvolvimento ágil de APIs RESTful.

## Material de Apoio

- [Documentação oficial do FastAPI](https://fastapi.tiangolo.com/)
- [Tutorial completo passo a passo](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI — GitHub](https://github.com/tiangolo/fastapi)
- [Awesome FastAPI — Lista curada de recursos](https://github.com/mjhea0/awesome-fastapi)
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
- [Real Python — FastAPI Tutorial](https://realpython.com/fastapi-python-web-apis/)
