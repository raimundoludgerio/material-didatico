from flask import request, render_template
from . import bp
from .forms import ProjetoForm
@bp.route('/cadastro', methods=["GET", "POST"])
def cadastro_usuario():
    if request.method == "POST":
        print("Enviado!")
    # 4. Retornar o conteúdo da resposta
    return render_template("cadastro.html")


@bp.route('/projeto', methods=["GET", "POST"])
def cadastro_projeto():
    formulario = ProjetoForm()
    return render_template("projeto.html", formulario=formulario)
