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

# Função para adicionar um livro
def adicionar_livro(titulo, autor, genero):
    cursor.execute('''
    INSERT INTO livros (titulo, autor, genero, disponivel)
    VALUES (?, ?, ?, ?)
    ''', (titulo, autor, genero, True))
    conn.commit()
    print(f"Livro '{titulo}' adicionado com sucesso!")

# Função para listar livros
def listar_livros():
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    print("Livros disponíveis na biblioteca:")
    for livro in livros:
        status = "Disponível" if livro[4] else "Indisponível"
        print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Gênero: {livro[3]}, Status: {status}")

# Exemplo de uso
adicionar_livro("O Alquimista", "Paulo Coelho", "Ficção")
adicionar_livro("Python para Todos", "Charles Severance", "Tecnologia")
listar_livros()

# Fechar conexão com o banco de dados
conn.close()
