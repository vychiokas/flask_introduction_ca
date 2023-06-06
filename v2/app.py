
import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
print("db initiated")


from models import Child, Father
import forms

print("imported forms and models")

@app.route("/children", methods=["GET", "POST"])
def get_all_children():
    db.create_all()
    children = Child.query.all()
    return render_template("children.html", children=children)

@app.route("/new_child", methods=["GET", "POST"])
def new_child():
    with app.app_context():
        db.create_all()
        form = forms.ChildForm()
        if form.validate_on_submit():
            new_child = Child(name=form.name.data,
                            surname=form.surname.data)
            db.session.add(new_child)
            db.session.commit()
            return redirect(url_for("get_all_children"))
        return render_template("add_child.html", form=form)


@app.route("/new_father", methods=["GET", "POST"])
def new_parent():
    with app.app_context():
        db.create_all()
        form = forms.FatherForm()
        if form.validate_on_submit():
            new_father = Father(name=form.name.data,
                                surname=form.surname.data,
                                child_id=form.child.data.id)
            db.session.add(new_father)
            db.session.commit()
            return "father created"
        return render_template("add_father.html", form=form)

