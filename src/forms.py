from .acceuil import app
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms.validators import DataRequired

class createUser(FlaskForm):
    username = StringField('username', validators=[DataRequired('Ce champ est requis')], min=5)
    login = EmailField('login')
    pseudo = StringField('pseudo')
