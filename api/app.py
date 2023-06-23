from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from api.models import db, User, Channel, Message
import os
import pusher
import uuid
import operator
import datetime
import git

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username=os.getenv('USERNAME'),
    password=os.getenv('PASSWORD'),
    hostname=os.getenv('HOSTNAME'),
    databasename=os.getenv('DATABASE'),
) 

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
CORS(app)

pusher = pusher.Pusher(
    app_id=os.getenv('PUSHER_APP_ID'),
    key=os.getenv('PUSHER_KEY'),
    secret=os.getenv('PUSHER_SECRET'),
    cluster=os.getenv('PUSHER_CLUSTER'),
    ssl=True)


@app.route("/")
def main():
    return "Hello"



@app.route("/updateServer", methods = ['POST'])
def updateServer():
    repo = git.Repo("/home/Balamurugan1234/chatApp");
    origin = repo.remotes.origin
    origin.pull()

    return 'Updated Successfully', 200

@app.route("/userlist", methods = ["GET"])
def userlist():
    users = User.query.all()
    return jsonify(
        [{"name" : user.name} for user in users]
    )

@app.route("/register", methods = ["POST"])
def register():
    data = request.get_json()
    
    user = User.query.filter_by(name = data["name"]).first()

    if user:
        return jsonify(
            {"message" : "user already exist",
             "status" : "failed"}
        )

    user = User(name=data["name"], 
                password=generate_password_hash(data["password"]))

    db.session.add(user)
    db.session.commit()

    return jsonify(
        {"message" : "user registered successfully",
         "status" : "success"}
    )

@app.route("/login", methods = ["POST"])
def login():
    return jsonify(
        
    )

@app.route("/start/<sender>/<receiver>", methods=["POST"])
def start(sender, receiver):
    
    channel = Channel.query.filter(Channel.user1.in_([sender, receiver])).filter(Channel.user2.in_([sender, receiver])).first()

    if not channel:
        channel = Channel(str(uuid.uuid4()), 
                          user1=sender,
                          user2=receiver)
        db.session.add(channel)
        db.session.commit()

        chat_channel = channel.channelid
    
    else:
        chat_channel = channel.channelid
    
    data = {
        "sender" : sender,
        "receiver" : receiver,
        "channel" : chat_channel
    }

    pusher.trigger(receiver, "new_chat", data)

    return data

@app.route("/message/<sender>/<receiver>", methods = ["POST"])
def message(sender, receiver):
    data = request.get_json()
    new_message = Message(str(uuid.uuid4()), sender, receiver, data["channel"], data["message"], datetime.datetime.now())

    db.session.add(new_message)
    db.session.commit()

    message = {
        "sender" : sender,
        "receiver" : receiver,
        "message" : data["message"],
        "channel" : data["channel"]
    }

    pusher.trigger(data["channel"], "new_message", message)

    return jsonify(message)

@app.route("/allmessages/<sender>/<receiver>", methods = ["GET"])
def allmessages(sender, receiver):
    channel = Channel.query.filter(Channel.user1.in_([sender, receiver])).filter(Channel.user2.in_([sender, receiver])).first()

    if not channel:
        return jsonify([])

    else:
        messages = Message.query.filter_by(channelid = channel.channelid).all()

        response = [{"sender" : message.senderid, "receiver" : message.receiverid, "body" : message.body, "timestamp" : message.timestamp} for message in messages]
        response.sort(key=operator.itemgetter('timestamp'))
                
        return response
