from flask import Flask, render_template, request, session

from utils import json_manager

app = Flask(__name__)
app.secret_key = 'NyNpVOZCMICdqIbrj2h4'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        print("Aqui criamos a seção")
        login = request.form.get("login")
        senha = request.form.get("senha")
        print(login, senha)
        session["login"] = login
        session["senha"] = senha
    return render_template("login.html")

@app.route("/produtos", methods = ["GET", "POST"])
def produtos():
    return render_template("produtos.html")

@app.route("/produto", methods = ["GET", "POST"])
def produto():
    if request.method == "POST":
        print("enviado via post")
    return render_template("cadastro.html")

@app.route("/cadastro_produto", methods=["GET", "POST"])
def cadastro_produto():
    if request.method == "POST":
        print("enviado via post")
    return render_template("cadastro_produto.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)
