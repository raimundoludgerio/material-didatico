from flask import Blueprint

bp = Blueprint("contato", __name__, template_folder="../../templates/contato")

from . import routes