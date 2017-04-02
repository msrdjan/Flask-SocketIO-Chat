from flask import Flask
from flask_socketio import SocketIO

# TODO: Check - Resolves "RuntimeError: Redis requires a monkey patched socket library to work with gevent"
from gevent import monkey
monkey.patch_all()

socketio = SocketIO()


def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'gjr39dkjn344_!67#'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # TODO: App instances connect to Redis server on one of the instances
    socketio.init_app(app, message_queue='redis://')
    return app
