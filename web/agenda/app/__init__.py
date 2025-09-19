from flask import Flask

def create_app():
    # Cria a instância da aplicação Flask
    app = Flask(__name__, template_folder='../templates')
    #app.config['SECRET_KEY'] = 'chave-super-secreta'

    from .contato import bp as contato_bp
    app.register_blueprint(contato_bp, url_prefix="/contato")

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
