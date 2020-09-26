from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

from run import hair_colors, eye_colors


class TagSelectForm(FlaskForm):
    hair_color = SelectField('Hair Color', choices=hair_colors)
    eye_color = SelectField('Eye Color', choices=eye_colors)
    submit = SubmitField('Submit')
    