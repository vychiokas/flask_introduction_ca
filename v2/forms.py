from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from models import Child


def child_query():
    return Child.query

class FatherForm(FlaskForm):
    name = StringField('name', [DataRequired()])
    surname = StringField('surname', [DataRequired()])
    child = QuerySelectField(query_factory=child_query,
                              allow_blank=True,
                              get_label="id",
                              get_pk=lambda obj: str(obj))
    submit = SubmitField('submit')


class ChildForm(FlaskForm):
    name = StringField('name', [DataRequired()])
    surname = StringField('surname', [DataRequired()])
    submit = SubmitField('submit')