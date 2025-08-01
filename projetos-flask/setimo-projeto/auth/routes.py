from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from utils import load_data

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        authors = load_data('data/authors.json')
        for author in authors:
            if author['username'] == username and author['password'] == password:
                session['username'] = username
                return redirect(url_for('posts.list_posts'))

        flash('Usuário ou senha inválidos')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('auth.login'))
