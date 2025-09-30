from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email



class RegisterForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[
        DataRequired(),
        Length(min=3, max=25, message="O nome de usuário deve ter entre 3 e 25 caracteres.")
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(),
        Length(min=6, message="A senha deve ter pelo menos 6 caracteres.")
    ])
    confirm_password = PasswordField('Confirme a Senha', validators=[
        DataRequired(),
        EqualTo('password', message='As senhas devem ser iguais.')
    ])
    submit = SubmitField('Cadastrar')