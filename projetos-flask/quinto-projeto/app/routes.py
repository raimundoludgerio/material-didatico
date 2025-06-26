from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .models import autenticar_usuario

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')
"""
    GET => RECUPERAR DADOS, 
    POST => ENVIAR ALGO PARA SER SALVO OU EM ROTAS DE LOGIN, 
    PUT => ATUALIZAR OS DADOS,
    PATCH => ATUALIZAR OS DADOS,
    DELETE => APAGAR OS DADOS

"""
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        if autenticar_usuario(login, senha):
            session["usuario"] = {"login": login, "senha": senha}
            return redirect(url_for('main.home'))
        else:
            flash('Usuário ou senha inválidos.')
    return render_template('login.html')