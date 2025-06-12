from flask import Flask, render_template
app = Flask(__name__)

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


@app.route('/cadastro')
def adicionar():
    return render_template("cadastro.html")

@app.route('/busca')
def buscar():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')
    return f"Seu nome: {nome} e {sobrenome}"

@app.route('/lista')
def buscar():
    lista = request.args.getList('lista')
    return f"Seu nome:{lista}"


if __name__ == '__main__':
    app.run(debug=True)
