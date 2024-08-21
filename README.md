
# ConsultaSQL

Este script em Python foi desenvolvido para realizar consultas SQL em um banco de dados PostgreSQL e salvar os resultados em um arquivo CSV. Ele utiliza as bibliotecas `pandas` para manipulação de dados, `psycopg2` para conexão com o banco de dados e `python-dotenv` para carregar variáveis de ambiente.

## Estrutura do Projeto

O script é organizado em uma classe chamada `ConsultaSQL`, que encapsula toda a lógica necessária para se conectar ao banco de dados, executar consultas, salvar os resultados e gerenciar a conexão.

### Classes e Métodos

#### Classe: `ConsultaSQL`

- **`__init__(self)`**: Método construtor que inicializa a classe e carrega as variáveis de ambiente do arquivo `.env`.

- **`connect(self)`**: Método que estabelece a conexão com o banco de dados usando as variáveis de ambiente. A conexão é estabelecida apenas uma vez.

- **`disconnect(self)`**: Método que encerra a conexão com o banco de dados, se existir.

- **`execute_query(self, query)`**: Método que executa a consulta SQL fornecida e retorna os resultados como um DataFrame do pandas. Se a conexão não tiver sido estabelecida, lança um erro.

- **`save_to_csv(self, df, file_path)`**: Método que salva o DataFrame fornecido em um arquivo CSV no caminho especificado.

- **`run(self, query, output_file)`**: Método principal que executa a sequência de operações: conecta ao banco de dados, executa a consulta SQL, salva os resultados em um arquivo CSV e desconecta do banco de dados.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `pandas`
  - `psycopg2`
  - `python-dotenv`

Você pode instalar as dependências necessárias utilizando o seguinte comando:

```bash
pip install pandas psycopg2-binary python-dotenv
```

## Configuração

O script depende de variáveis de ambiente para se conectar ao banco de dados. Essas variáveis devem ser definidas em um arquivo `.env` localizado no mesmo diretório do script. O arquivo `.env` deve ter o seguinte formato:

```env
DB_NAME=nome_do_banco
DB_USER=usuario_do_banco
DB_PASSWORD=senha_do_banco
DB_HOST=endereco_do_host
DB_PORT=porta_do_banco
```

Substitua os valores conforme necessário para a sua configuração de banco de dados.

## Uso

Para utilizar o script, você deve criar uma instância da classe `ConsultaSQL` e chamar o método `run` passando a consulta SQL que deseja executar e o caminho do arquivo CSV onde os resultados serão salvos. Exemplo:

```python
from postdatabase.consulta_sql import ConsultaSQL

# Cria uma instância da classe
consulta = ConsultaSQL()

# Define a consulta SQL e o caminho do arquivo de saída
query = "SELECT * FROM tabela_exemplo;"
output_file = "resultados.csv"

# Executa a consulta e salva os resultados
consulta.run(query, output_file)
```

Isso irá conectar ao banco de dados, executar a consulta SQL, salvar os resultados no arquivo `resultados.csv` e desconectar do banco.

## Instalação

Este projeto utiliza [Poetry](https://python-poetry.org/) para gerenciar as dependências e o ambiente virtual. Para configurar o projeto em sua máquina, siga os passos abaixo:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/gabrielmango/PostDatabase.git
   ```

2. **Instale o Poetry:**

   Se você ainda não tem o Poetry instalado, pode instalá-lo utilizando o comando:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   ou siga as instruções disponíveis na [documentação oficial](https://python-poetry.org/docs/#installation).

3. **Instale as dependências do projeto:**

   Com o Poetry instalado, execute o seguinte comando para instalar todas as dependências listadas no arquivo `pyproject.toml`:

   ```bash
   poetry install
   ```

   Este comando criará automaticamente um ambiente virtual e instalará todas as dependências necessárias.

4. **Ative o ambiente virtual:**

   Para ativar o ambiente virtual criado pelo Poetry, use o comando:

   ```bash
   poetry shell
   ```


Isso completará a instalação e configuração do projeto em sua máquina.

## Erros Comuns

- **Conexão não estabelecida**: Certifique-se de que as variáveis de ambiente estão corretamente configuradas no arquivo `.env` e que o banco de dados está acessível.

- **Erro de sintaxe SQL**: Verifique se a consulta SQL está correta e compatível com o banco de dados PostgreSQL.

## Contribuições

Sinta-se à vontade para abrir issues ou pull requests se encontrar problemas ou quiser sugerir melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
