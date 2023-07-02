from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    name = db.Column(db.String(100), primary_key = True, autoincrement = False)
    password = db.Column(db.String(256))

    def __init__(self, name, password):
        self.name = name
        self.password = password

class Message(db.Model):
    __tablename__ = "message"
    messageid = db.Column(db.String(36), primary_key = True, autoincrement = False)
    senderid = db.Column(db.String(100))
    receiverid = db.Column(db.String(100))
    channelid = db.Column(db.String(36))
    body = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime)

    def __init__(self, messageid, senderid, receiverid, channelid, body, timestamp):
        self.messageid = messageid
        self.senderid = senderid
        self.receiverid = receiverid
        self.channelid = channelid
        self.body = body
        self.timestamp = timestamp

class Channel(db.Model):
    __tablename__ = "channel"
    channelid = db.Column(db.String(200), primary_key = True, autoincrement = False)
    user1 = db.Column(db.String(100))
    user2 = db.Column(db.String(100))

    def __init__ (self, channelid, user1, user2):
        self.channelid = channelid
        self.user1 = user1
        self.user2 = user2

class GroupTable(db.Model):
    __tablename__ = "groupTable"
    id = db.Column(db.Integer, primary_key = True)
    groupname = db.Column(db.String(100))
    username = db.Column(db.String(100))
    
    def __init__(self, groupname, username):
        self.groupname = groupname
        self.username = username

class GroupChannel(db.Model):
    __tablename__ = "groupChannel"
    channelid = db.Column(db.String(100), primary_key = True, autoincrement = False)
    groupname = db.Column(db.String(100))

    def __init__(self, channelid, groupname):
        self.channelid = channelid
        self.groupname = groupname

class GroupMessage(db.Model):
    __tablename__ = "groupMessage"
    messageid = db.Column(db.String(100), primary_key = True, autoincrement = False)
    senderid = db.Column(db.String(100))
    channelid = db.Column(db.String(100))
    groupname = db.Column(db.String(100))
    body = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime)

    def __init__(self, messageid, senderid, channelid, groupname, body, timestamp):
        self.messageid = messageid
        self.senderid = senderid
        self.channelid = channelid
        self.groupname = groupname
        self.body = body
        self.timestamp = timestamp

    def as_dict(self):
        return {c.name : str(getattr(self, c.name)) for c in self.__table__.columns }
