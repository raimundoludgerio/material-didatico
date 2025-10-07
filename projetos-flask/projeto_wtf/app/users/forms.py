from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Optional, regexp
import email_validator

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar de mim')
    submit = SubmitField('Entrar')

class Login2(FlaskForm):
    username = StringField("Usuário", validators=[DataRequired(), Length(min=5)])
    senha = PasswordField("Senha", validators=[DataRequired()])
    botao = SubmitField("Logar")

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
       pass
    
    def validate_email(self, email):
        pass
        
class ContactForm(FlaskForm):
    name = StringField('Nome', validators=[
        DataRequired(message='O nome é obrigatório'),
        Length(min=2, max=50, message='O nome deve ter entre 2 e 50 caracteres')
    ])
    
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message='Digite um email válido')
    ])
    
    phone = StringField('Telefone', validators=[
        Optional(),
        regexp(r'^\(\d{2}\)\d{4,5}-\d{4}$', message='Formato: (11)99999-9999')
    ])
    
    message = TextAreaField('Mensagem', validators=[
        DataRequired(),
        Length(min=10, max=500, message='A mensagem deve ter entre 10 e 500 caracteres')
    ])
    
    category = SelectField('Categoria', choices=[
        ('duvida', 'Dúvida'),
        ('sugestao', 'Sugestão'),
        ('reclamacao', 'Reclamação'),
        ('elogio', 'Elogio')
    ], validators=[DataRequired()])
    
    submit = SubmitField('Enviar Mensagem')