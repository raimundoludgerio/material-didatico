from flask import Flask, render_template_string
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'

class TestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestForm()
    if form.validate_on_submit():
        return 'Formulário válido!'
    return render_template_string('''
        <form method="POST">
            {{ form.hidden_tag() }}
            {{ form.email.label }} {{ form.email() }}
            {{ form.submit() }}
        </form>
    ''', form=form)

if __name__ == "__main__":
    app.run(debug=True)
