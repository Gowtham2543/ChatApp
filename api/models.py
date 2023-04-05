from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    userid = db.Column(db.String(36), primary_key = True, autoincrement = False)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(256))

    def __init__(self, userid, name, email, password):
        self.userid = userid
        self.name = name
        self.email = email
        self.password = password

class Message(db.Model):
    __tablename__ = "message"
    messageid = db.Column(db.String(36), primary_key = True, autoincrement = False)
    sender_id = db.Column(db.String(36))
    receiver_id = db.Column(db.String(36))
    body = db.Column(db.String(100))

class Channel(db.Model):
    __tablename__ = "channel"
    channelid = db.Column(db.String(73), primary_key = True, autoincrement = False)
    user1 = db.Column(db.String(36))
    user2 = db.Column(db.String(36))
    