from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def incial():
    return 'Olá Mundo!'

@app.route('/add')
def adicionar():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
