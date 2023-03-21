from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def handle_message(message):
    print("Message : " + message)

    send(message, broadcast=True)

@app.route("/")
def main():
    return "HEllo"

if __name__ == "__main__":
    socketio.run(app, host="localhost")
