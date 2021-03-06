from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room') if 'room' in session else message['room'] if 'room' in message else 'None'
    session['room'] = room
    name = session.get('name') if 'name' in session else message['name'] if 'name' in message else 'None'
    session['name'] = name
    join_room(room)
    emit('status', {'msg': name + ' has entered the room.'}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room') if 'room' in session else 'None'
    name = session.get('name') if 'name' in session else 'None'
    msg = message['msg'] if 'msg' in message else message
    emit('message', {'msg': name + ':' + msg}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room') if 'room' in session else 'None'
    name = session.get('name') if 'name' in session else 'None'
    leave_room(room)
    emit('status', {'msg': name + ' has left the room.'}, room=room)
