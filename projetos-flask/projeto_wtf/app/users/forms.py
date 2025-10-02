from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import email_validator

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')

class RegistrationForm(FlaskForm):
    username = StringField('Nome de Usuário', 
                          validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', 
                       validators=[DataRequired(), Email()])
    password = PasswordField('Senha', 
                           validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Senha', 
                                   validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Cadastrar')
    
    # Validação personalizada
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este nome de usuário já está em uso.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este email já está cadastrado.')