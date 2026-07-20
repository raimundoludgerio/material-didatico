from flask import Flask, render_template, request, flash, redirect, url_for
from utils import json_manager

app = Flask(__name__)
app.secret_key = 'NyNpVOZCMICdqIbrj2h4'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/produtos", methods = ["GET", "POST"])
def produtos():
    return render_template("produtos.html")

@app.route("/produto", methods = ["GET", "POST"])
def produto():
    if request.method == "POST":
        nome_produto = request.form.get("nomeProduto").strip()
        print(nome_produto)
        if nome_produto == "":
            flash("Campo obrigatório", "danger")
            return redirect(url_for('produto'))
        json_manager.salvar_produto(nome_produto)
        flash("Produto Cadastrado com sucesso", "success")
    return render_template("cadastro.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)
