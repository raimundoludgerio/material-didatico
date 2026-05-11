from flask import Flask, render_template, request
from datetime import datetime
app = Flask(__name__)
users = []

@app.route('/')
def home():
    return f'<h1> Essa é a página inicial </h1>'

@app.route('/<nome>')
def nome(nome):
    return f'Olá, {nome}!'

@app.route('/<int:pagina>')
def pagina(pagina):
    return f'A página é: {pagina}!'

@app.route('/<float:preco>')
def preco(preco):
    return f'O valor total é: R${preco}!'



@app.route('/<path:arquivo>')
def file(arquivo):
    return f'Solicitado {arquivo}!'


@app.route('/cadastro', methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        nome = request.form["nome"]
        hora = datetime.now().hour
        user = {"id": 0, "nome":nome, "hora": str(hora)}
        users.append(user)
        return f"Usuario {nome} cadastrado com sucesso"
    return render_template("cadastro.html")

@app.route('/busca')
def buscar():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    return f"Seu nome: {nome} e {sobrenome}"

@app.route('/lista')
def listar():
    #lista = request.args.getList('lista')
    return render_template("listagem.html", users=users)


if __name__ == '__main__':
    app.run(debug=True)
