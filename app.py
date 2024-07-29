from flask import Flask
from src.main.routes.pix_route import pix_route_bp
from flask_socketio import SocketIO
from utils import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

db.init_app(app)
socketio = SocketIO(app)

app.register_blueprint(pix_route_bp)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)