from flask import render_template, flash, redirect, url_for
from . import bp
from app.forms.login_form import LoginForm
from app.forms.register_form import RegisterForm
from ..model.user import User


@bp.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.find_by_email(login_form.email.data)
        flash(f'Bem-vindo, {user.username}!', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html', form=login_form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        if not new_user:
            flash('Usuário já existe com este email ou nome de usuário.', 'danger')
            return render_template('auth/register.html', form=form)
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)