from flask import Flask


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='../templates')
    app.config['SECRET_KEY'] = 'chave-secreta' # necessário para o CSRF

    from .users import bp as user_bp
    app.register_blueprint(user_bp)
    
    return app