# Importando as coisas básicas do Flask
from flask import Flask
from rotas import rotas  # Importando as rotas separadas
import banco  # Chamando o banco de dados, porque né... tem que guardar as notas em algum lugar

app = Flask(__name__)  # Criando o app Flask
app.register_blueprint(rotas)  # Registrando as rotas do app

if __name__ == '__main__':
    banco.inicializar_banco()  # Garantindo que o banco já vai estar pronto
    app.run(debug=True)  # Rodando o servidor no modo debug (mostra erros bonitinhos)