from wtforms import Form, StringField, validators, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class MailForm(FlaskForm):
    name = StringField("Imię i Nazwisko", validators=[InputRequired()])
    email = StringField("E-Mail", validators=[InputRequired()])
    topic = StringField("Temat", validators=[InputRequired()])
    text = TextAreaField("Treść", validators=[InputRequired()])