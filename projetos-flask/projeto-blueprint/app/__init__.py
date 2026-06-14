# 1. Importar o Flask
from flask import Flask

def create_app():
    app = Flask(__name__, static_folder="../static")
    app["secret_key"] = "qualquer-coisa"

    from .auth import blueprint as auth_bp
    app.register_blueprint(auth_bp)

    from .users import bp as users_bp
    app.register_blueprint(users_bp)


    return app