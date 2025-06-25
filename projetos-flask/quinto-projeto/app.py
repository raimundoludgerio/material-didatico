from flask import Flask, render_template, request
from model.models import Usuario

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    user_login = request.form.get('login')
    user_senha = request.form.get('senha')
    usuario_login = Usuario()

    

    
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)