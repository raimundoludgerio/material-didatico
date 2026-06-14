from flask import render_template
from . import blueprint



@blueprint.route("/login")
def login():
    # 4. Retornar o conteúdo da resposta
    return render_template("login.html")

@blueprint.route("/logout")
def logout():
    print("Desconectado")
