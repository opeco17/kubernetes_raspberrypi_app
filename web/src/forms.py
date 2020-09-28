from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

from config import Config


class TagSelectForm(FlaskForm):
    hair_color = SelectField('Hair Color', choices=Config.HAIR_COLORS)
    submit = SubmitField('Submit')
    