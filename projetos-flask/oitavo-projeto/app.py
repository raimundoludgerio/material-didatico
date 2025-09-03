from flask import Flask, render_template, request, redirect, url_for, flash
from models.user import verificar_usuario
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form["username"]
        password = request.form["password"]
        if(verificar_usuario(login, password)):
            return redirect(url_for('home'))
        else:
            flash("Usuário Inválido!")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
