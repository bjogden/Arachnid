from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Optional


class ArachnidForm(FlaskForm):
    screen_width = IntegerField('Screen width', validators=[Optional()], default=2560)
    screen_height = IntegerField('Screen height', validators=[Optional()], default=1440)
    urls = TextAreaField('URLs', validators=[DataRequired()])
