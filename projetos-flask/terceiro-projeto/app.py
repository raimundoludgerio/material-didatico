from flask import Flask, render_template
import datetime
app = Flask(__name__)

# Dados de exemplo (normalmente viriam de um banco de dados)
posts = [
    {
        'id': 1,
        'title': 'Primeiro Post',
        'content': 'Este é o conteúdo do primeiro post.',
        'author': 'João Silva'
    },
    {
        'id': 2,
        'title': 'Segundo Post',
        'content': 'Este é o conteúdo do segundo post.',
        'author': 'Maria Souza'
    }
]

@app.route('/')
def home():
    hora_atual = datetime.datetime.now().hour
    return render_template('index.html', hora_atual=hora_atual)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    # Encontrar o post com o ID correspondente
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post não encontrado", 404
@app.route('/login', methods=['POST'])
def login(post_id):
    # Encontrar o post com o ID correspondente
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post não encontrado", 404




if __name__ == '__main__':
    app.run(debug=True)