# Importando o Flask e funções que vamos precisar
from flask import Blueprint, render_template, request, redirect, url_for
from banco import obter_notas, adicionar_nota, apagar_nota, editar_nota

rotas = Blueprint('rotas', __name__)  # Criando um Blueprint (basicamente um grupo de rotas)

@rotas.route('/')
def index():
    notas = obter_notas()  # Pegando as notas do banco
    return render_template('index.html', notas=notas)  # Mandando as notas pra página

@rotas.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form['titulo']  # Pegando o título da nota
    detalhes = request.form['detalhes']  # Pegando os detalhes
    adicionar_nota(titulo, detalhes)  # Salvando no banco
    return redirect(url_for('rotas.index'))  # Voltando pra página principal

@rotas.route('/apagar/<int:id>')
def apagar(id):
    apagar_nota(id)  # Chamando a função que remove do banco
    return redirect(url_for('rotas.index'))



@rotas.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']
    editar_nota(id, titulo, detalhes)
    return redirect(url_for('rotas.index'))