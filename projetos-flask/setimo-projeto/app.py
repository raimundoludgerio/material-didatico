from flask import Flask
from auth.routes import auth_bp
from authors.routes import authors_bp
from posters.routes import posts_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'segredo_super_simples'

    app.register_blueprint(auth_bp)
    app.register_blueprint(authors_bp)
    app.register_blueprint(posts_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)