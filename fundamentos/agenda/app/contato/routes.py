from flask import render_template
from . import bp


@bp.route("/cadastro")
def cadastro_usuario():
    return render_template("contato/contatos.html")



@bp.route("/listagem")
def listagem_usuario():
    return render_template("contato/listagem.html")