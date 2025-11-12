from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ProjetoForm(FlaskForm):
    nome = StringField("Nome", validators=[])
    descricao = StringField("Descrição", validators=[])
    botao = SubmitField("Cadastrar")