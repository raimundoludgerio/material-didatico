from flask import Flask, render_template, request, flash, redirect, url_for, session
from controller import usuario_controller

app = Flask(__name__)
app.secret_key = 'E4NgVIbgDw'


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")



@app.route("/perfil")
def perfil():
    usuario_logado = session.get("user")
    if usuario_logado:
        user = usuario_controller.recuperar_usuario(usuario_logado)
        print(user)
        return render_template("perfil.html", usuario=user)
    return redirect(url_for("login"))



@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form["email"]
        senha = request.form["senha"]
        if(usuario_controller.valida_login(login, senha)):
            session["user"] = login
            flash("Login realizado com sucesso", "success")
            return redirect(url_for("perfil"))
        else:
            flash("Verifique os dados e tente novamente", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('user', None)
    flash("Usuário Desconectado", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
