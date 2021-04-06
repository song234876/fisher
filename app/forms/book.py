from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class ClassForm(Form):
    name = StringField(validators=[DataRequired(), Length(min=1, max=15)])
    age = IntegerField(validators=[DataRequired(), NumberRange(min=1)])
