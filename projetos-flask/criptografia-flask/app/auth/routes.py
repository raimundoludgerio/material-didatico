from flask import render_template, flash, redirect, url_for
from . import bp
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm

@bp.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html', form=login_form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Aqui você adicionaria o usuário ao banco de dados
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)