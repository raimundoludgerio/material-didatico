from flask import Flask, render_template, request
from controllers.produto_controller import get_produtos, cadastrar_produto

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/produtos')
def produtos():
    produtos = get_produtos()
    return render_template('produto.html', produtos=produtos)

@app.route('/cadastrar_produto', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    descricao = request.form['descricao']
    preco = float(request.form['preco'])
    cadastrar_produto(nome, descricao, preco)
    return "Produto cadastrado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
