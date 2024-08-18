````markdown
# Rastreabilidade de Subconjuntos

Este projeto é uma aplicação web desenvolvida com **FastAPI** e **HTML**, que permite a rastreabilidade de subconjuntos, possibilitando o registro e gerenciamento de dados como nome, linha de produção, defeitos, técnico responsável, entre outros.

## Funcionalidades

- **Registro de subconjuntos**: O usuário pode selecionar um subconjunto de uma lista, especificar o movimento, a linha de produção, o defeito identificado, o técnico responsável, e adicionar comentários.
- **Envio de dados via formulário HTML**: Os dados são enviados e armazenados em um banco de dados MySQL através de requisições POST.
- **Leitura de registros**: É possível consultar registros de subconjuntos armazenados no banco de dados.

## Tecnologias Utilizadas

- **Backend**: FastAPI, SQLAlchemy
- **Frontend**: HTML, JavaScript
- **Banco de Dados**: MySQL
- **ORM**: SQLAlchemy para interagir com o banco de dados.

## Instalação

### Pré-requisitos

- Python 3.9+
- MySQL
- Pip (para gerenciar dependências)
- MySQL connector para Python (`pymysql`)

### Passos

1. Clone este repositório:

```bash
git clone https://github.com/usuario/repositorio.git
cd repositorio
```
````

2. Instale as dependências necessárias:

```bash
pip install fastapi sqlalchemy pymysql uvicorn
```

3. Configure a conexão com o banco de dados MySQL no arquivo principal, substituindo as credenciais no parâmetro `DATABASE_URL`:

```python
DATABASE_URL = "mysql+pymysql://usuario:senha@host/database"
```

4. Execute a aplicação:

```bash
uvicorn main:app --reload
```

5. Acesse a aplicação no navegador através de:

```
http://localhost:8000
```

## Endpoints da API

### Criar um subconjunto

`POST /subconjuntos/`

- **Corpo da requisição** (exemplo):

```json
{
  "nome": "Amortecimento do Plato",
  "linha": 591,
  "idsub": 12345,
  "movimento": "emReparo",
  "data": "2023-01-01",
  "defeito": "Garra quebrada",
  "tecnico": "João Silva",
  "comentario": "Comentário adicional"
}
```

### Listar subconjuntos

`GET /subconjuntos/`

- **Parâmetros**: `skip` (padrão: 0), `limit` (padrão: 10)
- Retorna uma lista de subconjuntos registrados.

## Estrutura do Banco de Dados

A tabela `subconjuntos` contém os seguintes campos:

- `id` (inteiro, chave primária)
- `dataehora` (data e hora do registro, gerada automaticamente)
- `nome` (string)
- `linha` (inteiro)
- `idsub` (inteiro)
- `movimento` (string)
- `data` (data)
- `defeito` (texto)
- `tecnico` (texto)
- `comentario` (texto)

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
