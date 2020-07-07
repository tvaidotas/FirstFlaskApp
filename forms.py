from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class PostsForm(FlaskForm):
    f_name = StringField(
        'First name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    l_name = StringField(
        'Last name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    title = StringField(
        'Title',
        validators=[
            DataRequired(),
            Length(min=4, max=100)
        ]
    )

    content = StringField(
        'Content',
        validators=[
            DataRequired(),
            Length(min=4, max=300)
        ]
    )

    submit = SubmitField('Make a Post')
