from flask import Flask
import os
from dotenv import load_dotenv
import pusher
from models import db

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

