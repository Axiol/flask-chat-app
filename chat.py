from distutils.log import debug
from gc import callbacks
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
socketio = SocketIO(app)

@app.route('/')
def chat():
  return render_template('chat.html')

def messageReceived(methods=['GET', 'POST']):
  print('Message received!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
  print ('Received my event: ' + str(json))
  socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
  socketio.run(app, port=3000, debug=True)