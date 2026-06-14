import os
import models
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Chave secreta necessária para usar sessões e o flash messages
app.secret_key = 'uma_chave_secreta_muito_segura'


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        users = models.load_users()
        
        if username in users:
            flash('Este usuário já existe. Tente outro.', 'error')
            return redirect(url_for('register'))
        
        # Salvando o usuário com a senha criptografada (boa prática)
        user = {
            "username": username,
            "password": generate_password_hash(password) # Senha criptografada
        }
        users.append(user)
        models.save_users(users)
        
        flash('Cadastro realizado com sucesso! Faça seu login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        users = models.load_users()
        if len(users) == 0:
            flash('Usuário ou senha incorretos.', 'error')
            redirect(url_for('login'))
        # Verifica se o usuário existe e se a senha confere
        print(username)
        
        for user in users:
            print(user)
            print(check_password_hash(user['password'], password))
            if check_password_hash(user['password'], password):
                session['username'] = username
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Usuário ou senha incorretos.', 'error')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)