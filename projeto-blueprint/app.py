# 1. Importar o Flask
from flask import Flask, request, render_template

# 2. Criar uma instância do Flask
# __name__ é uma variável especial do Python que indica o nome do módulo atual.
# Flask a usa para saber onde encontrar outros arquivos necessários para a aplicação.
app = Flask(__name__)

# 3. Definir uma rota (URL) e a função de visualização associada
# O decorador @app.route('/') liga a URL raiz '/' à função 'index'.
@app.route('/')
def index():
    # 4. Retornar o conteúdo da resposta
    return "Olá, Mundo!"

@app.route('/login')
def login():
    # 4. Retornar o conteúdo da resposta
    return render_template("login.html")

@app.route('/cadastro', methods=["GET", "POST"])
def cadastro_projeto():
    if request.method == "POST":
        print("Enviado!")
    # 4. Retornar o conteúdo da resposta
    return render_template("cadastro.html")

# 5. Executar o aplicativo (se o script for executado diretamente)
if __name__ == '__main__':
    app.run(debug=True)