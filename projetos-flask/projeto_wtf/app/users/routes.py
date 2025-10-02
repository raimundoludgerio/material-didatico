from flask import flash, render_template, redirect, url_for
from . import bp
from .forms import RegistrationForm
@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Aqui você pode processar os dados, por exemplo, salvar no banco de dados
        flash(f'Conta criada para {form.username.data}!', 'success')
        # Redireciona para a mesma página ou para uma página de sucesso
        return redirect(url_for('register'))  
    return render_template('cadastro.html', title='Registrar', form=form)