# Sistema de Gerenciamento de Biblioteca

Este é um simples sistema de gerenciamento de biblioteca desenvolvido em Python, utilizando SQLite como banco de dados.

## Estrutura do Projeto

```
biblioteca.db
SistemadeGerenciamentodeBiblioteca.py
```

- `biblioteca.db`: Arquivo do banco de dados SQLite que armazena as informações dos livros.
- `SistemadeGerenciamentodeBiblioteca.py`: Script Python que contém a lógica do sistema de gerenciamento de biblioteca.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

1. **Adicionar Livro**: Adiciona um novo livro ao banco de dados.
2. **Listar Livros**: Lista todos os livros disponíveis na biblioteca.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Execute o script `SistemadeGerenciamentodeBiblioteca.py` utilizando o comando:

```sh
python SistemadeGerenciamentodeBiblioteca.py
```

## Código

### Conexão com o Banco de Dados

O script cria ou conecta ao banco de dados `biblioteca.db` e cria a tabela `livros` se ela não existir:

```python
import sqlite3

# Criar ou conectar ao banco de dados
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# Criar tabela de livros
cursor.execute('''
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    genero TEXT NOT NULL,
    disponivel BOOLEAN NOT NULL
)
''')
conn.commit()
```

### Função para Adicionar Livro

A função `adicionar_livro` adiciona um novo livro ao banco de dados:

```python
def adicionar_livro(titulo, autor, genero):
    cursor.execute('''
    INSERT INTO livros (titulo, autor, genero, disponivel)
    VALUES (?, ?, ?, ?)
    ''', (titulo, autor, genero, True))
    conn.commit()
    print(f"Livro '{titulo}' adicionado com sucesso!")
```

### Função para Listar Livros

A função `listar_livros` lista todos os livros disponíveis na biblioteca:

```python
def listar_livros():
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    print("Livros disponíveis na biblioteca:")
    for livro in livros:
        status = "Disponível" if livro[4] else "Indisponível"
        print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}, Status: {status}")
```

### Exemplo de Uso

O script adiciona dois livros de exemplo e lista todos os livros:

```python
# Exemplo de uso
adicionar_livro("O Alquimista", "Paulo Coelho", "Ficção")
adicionar_livro("Python para Todos", "Charles Severance", "Tecnologia")
listar_livros()
```

### Fechar Conexão com o Banco de Dados

Ao final, o script fecha a conexão com o banco de dados:

```python
# Fechar conexão com o banco de dados
conn.close()
```

## Contribuição

Sinta-se à vontade para contribuir com melhorias para este projeto. Para isso, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
