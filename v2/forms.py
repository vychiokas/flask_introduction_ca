from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
import app

def child_query():
    return app.Child.query

class FatherForm(FlaskForm):
    name = StringField('name', [DataRequired()])
    surname = StringField('surname', [DataRequired()])
    child = QuerySelectField(query_factory=child_query,
                              allow_blank=True,
                              get_label="name",
                              get_pk=lambda obj: str(obj))
    submit = SubmitField('submit')


class ChildForm(FlaskForm):
    name = StringField('name', [DataRequired()])
    surname = StringField('surname', [DataRequired()])
    submit = SubmitField('submit')