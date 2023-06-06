
import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import forms

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

    
class Father(db.Model):
    __tablename__ = "father"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String)
    surname = db.Column("surname", db.String)
    child_id = db.Column(db.Integer, db.ForeignKey("child.id"))
    child = db.relationship("Child")


class Child(db.Model):
    __tablename__ = "child"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String)
    surname = db.Column("surname", db.String)
    

@app.route("/new_child", methods=["GET", "POST"])
def new_child():
    db.create_all()
    forma = forms.ChildForm()
    if forma.validate_on_submit():
        new_child = Child(name=forma.name.data,
                          surname=forma.surname.data)
        db.session.add(new_child)
        db.session.commit()
        return "child created"
    return render_template("add_child.html", form=forma)


if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()