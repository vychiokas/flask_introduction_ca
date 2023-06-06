from app import Message, app, db


with app.app_context():
    jonas = db.session.get(Message, 1)
    db.session.delete(jonas)
    db.session.commit()
    print(Message.query.all())
