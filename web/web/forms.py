from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class ConfigForm(FlaskForm):
    message_text = TextAreaField('Mensagem', validators=[DataRequired()])
    interval_minutes = IntegerField('Intervalo (min)', default=60)
    valid_time_minutes = IntegerField('Validade (min)', default=10)
    random_min = FloatField('Mínimo aleatório', default=1.0)
    random_max = FloatField('Máximo aleatório', default=2.0)
    submit = SubmitField('Salvar')
