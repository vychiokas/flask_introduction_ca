from app import Message, app, db

with app.app_context():
    all_messages = Message.query.all()
    print(all_messages)

#  [Jonas - jonas@mail.com, Antanas - antanas@mail.lt, Juozas - juozukas@friends.lt, Bronius - bronka@yahoo.com]

    message_1 = db.session.get(Message, 1)
    print(message_1)

    message_antanas = Message.query.filter_by(name='Antanas')
    print(message_antanas.all())

# [Antanas - antanas@mail.lt]
# Jonas - jonas@mail.com