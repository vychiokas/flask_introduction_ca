from app import db

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