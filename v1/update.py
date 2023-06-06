from app import Message, app, db


with app.app_context():
    antanas = db.session.get(Message, 2)
    antanas.email = 'geras.zmogus@lrs.lt'
    db.session.add(antanas)
    db.session.commit()
    print(Message.query.all())
