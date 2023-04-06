from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from models import db, User
import os
import pusher

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:1234@localhost/Chat" 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

pusher = pusher.Pusher(
    app_id=os.getenv('PUSHER_APP_ID'),
    key=os.getenv('PUSHER_KEY'),
    secret=os.getenv('PUSHER_SECRET'),
    cluster=os.getenv('PUSHER_CLUSTER'),
    ssl=True)


@app.route("/")
def main():
    return "Hello"

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

    user = User(name = data["name"], password = generate_password_hash(data["password"]))

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

