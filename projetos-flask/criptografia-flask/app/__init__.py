from flask import Flask


def create_app():
    app = Flask(__name__, static_folder='static', template_folder='../templates')
    app.config['SECRET_KEY'] = 'chave-secreta'
    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app