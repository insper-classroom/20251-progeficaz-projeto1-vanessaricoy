import sqlite3  # Biblioteca de banco de dados do SQLite

# Criando o banco e a tabela se não existir
def inicializar_banco():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS notas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        detalhes TEXT NOT NULL)''')
    conexao.commit()
    conexao.close()

# Pegando todas as notas salvas
def obter_notas():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM notas")
    notas = cursor.fetchall()
    conexao.close()
    return notas

# Salvando uma nova nota
def adicionar_nota(titulo, detalhes):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO notas (titulo, detalhes) VALUES (?, ?)", (titulo, detalhes))
    conexao.commit()
    conexao.close()

# Apagar nota pelo ID
def apagar_nota(id):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM notas WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

# Editar nota pelo ID
def editar_nota(id, titulo, detalhes):
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE notas SET titulo = ?, detalhes = ? WHERE id = ?", (titulo, detalhes, id))
    conexao.commit()
    conexao.close()