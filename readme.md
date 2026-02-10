# FastAPI Project

## ▶️ Rodando o servidor

```bash
uvicorn main:app --reload
```

## ⚙️ Configuração Inicial

1. Instalar as dependências  
2. Instanciar o FastAPI  
3. Criar o arquivo das rotas (rota de auth / rota de order)  
4. Importar nossas rotas no `main.py`  
5. Criar um roteador para cada rota utilizando o `APIRouter`  
   - Definir o prefix para as rotas  
   - Definir tags para aparecer na documentação  
6. Informar ao `main` para utilizar os roteadores  


## 🛣️ Criação de Rotas

1. Utilizar um decorator junto com o roteador, passando o status HTTP e o endpoint  
2. Criar uma função assíncrona para a rota  


## 🗄️ Banco de Dados / ORM + Criação de Tabelas

1. Criação e conexão com o banco de dados  
2. Criar uma pasta/arquivo chamado `models`, onde será utilizada a ORM SQLAlchemy com banco SQLite  
3. Criar a constante `db` utilizando a função `create_engine` do SQLAlchemy, passando como parâmetro a URL do banco  

```python
db = create_engine("sqlite:///db/database.db")
```

4. Criar a `Base` do banco de dados utilizando `declarative_base`  
5. Criar as classes que representam as tabelas do banco  
   - Utilizar o atributo `__tablename__` para definir manualmente o nome da tabela  
   - Definir os campos de cada tabela  

6. Importar da ORM SQLAlchemy o `Column` para tipar os valores  
7. Importar os tipos de dados utilizados nas colunas, como `String`, `Integer`, `Boolean`, `Float`, `ForeignKey`  

Exemplo:
```python
id = Column("id", Integer)
```

8. Parâmetros importantes para criação das colunas:
   - `nullable=False` → campo obrigatório  
   - `primary_key=True` → chave primária  
   - `autoincrement=True` → incremento automático  
   - `default=False` → valor padrão  
   - `ForeignKey()` → relacionamento entre tabelas  

Exemplo:
```python
user = Column("user", ForeignKey("users.id"))
```

9. Criar a função `__init__`, responsável por inicializar os dados do objeto ao criar um novo registro.  
   Essa função não cria tabelas nem colunas.

10. Utilizar um ENUM semelhante ao TypeScript, instalando a biblioteca `sqlalchemy_utils`  


## 🧩 Configuração + Migrations (Alembic)

1. Instalar a biblioteca Alembic  
2. No arquivo `alembic.ini`, alterar a variável `sqlalchemy.url` para a URL do banco  
3. No arquivo `env.py`:
   - Importar `sys` e `os`
   - Adicionar o caminho raiz do projeto

```python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models import Base
target_metadata = Base.metadata
```

4. Gerar a migration:

```bash
alembic revision --autogenerate -m "initial migration"
```

Esse comando:
- Lê os models  
- Compara com o estado do banco  
- Gera um arquivo de migration  
- Não cria tabelas  
- Não aplica alterações no banco  
- Pode criar o arquivo `.db` vazio apenas por abrir a conexão  

5. Aplicar a migration:

```bash
alembic upgrade head
```

6. A cada alteração no banco, deve-se criar uma nova migration.
