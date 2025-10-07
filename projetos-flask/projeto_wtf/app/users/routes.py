from flask import flash, render_template, redirect, url_for
from . import bp
from .forms import RegistrationForm, LoginForm, Login2
@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Aqui você pode processar os dados, por exemplo, salvar no banco de dados
        flash(f'Conta criada para {form.username.data}!', 'success')
        # Redireciona para a mesma página ou para uma página de sucesso
        return redirect(url_for('register'))  
    return render_template('cadastro.html', title='Registrar', form=form)

@bp.route('/', methods=['GET'])
def index():
    return "página index"
@bp.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        # Simulação de autenticação
        email = form.email.data
        password = form.password.data
        
        # Em uma aplicação real, verifique no banco de dados
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('index'))
       
    return render_template('login.html', form=form)


@bp.route('/login2', methods=['GET', 'POST'])
def login2():
    formulario = Login2()
    if formulario.validate_on_submit():
        flash("Login realizado com sucesso")
        usuario = formulario.username.data
        password = formulario.senha.data
        usuario = {
            "user": usuario,
            "password": password
        }
        return render_template("home.html", user=usuario)
    return render_template("login2.html", formulario=formulario)
