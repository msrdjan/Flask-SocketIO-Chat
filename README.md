Flask-SocketIO-Chat
===================

A simple chat application that demonstrates how to structure a Flask-SocketIO application.

To run this application install the requirements in a virtual environment, run `python chat.py` and visit `http://localhost:5000` on one or more browser tabs.

If you prefer, you can also start the server using the Flask cli:

    $ FLASK_APP=chat.py flask run

Or, using `gevent` and `uWSGI` server:

	$ uwsgi --http :5000 --gevent 1000 --http-websockets --master --wsgi-file chat.py --callable app

Or, the same with included [Flask-SocketIO-Chat.ini](Flask-SocketIO-Chat.ini) `uWSGI` configuration file:

	$ uwsgi --ini Flask-SocketIO-Chat.ini

Or, configure Nginx and `systemd` by tweaking included [Flask-SocketIO-Chat.conf](Flask-SocketIO-Chat.conf) and [Flask-SocketIO-Chat.service](Flask-SocketIO-Chat.service) files, respectively.