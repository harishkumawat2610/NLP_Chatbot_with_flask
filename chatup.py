from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# https://flask-socketio.readthedocs.io/en/latest/
# https://github.com/socketio/socket.io-client
#https://www.analyticsvidhya.com/blog/2017/09/machine-learning-models-as-apis-using-flask/

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'jsbcfsbfjefebw237u3gdbdc'
socketio = SocketIO( app )

@app.route( '/' )
def hello():
  return render_template( './ChatApp.html' )

def messageRecived():
  print( 'message was received!!!' )

'''@socketio.on( 'my event' )
def handle_my_custom_event( json ):
  print( 'recived my event: ' + str( json ) )
  socketio.emit( 'my response', json, callback=messageRecived )'''

@socketio.on( 'my eventes' )
def handle_my_custom_event1( json1 ):
  import chatbot_final
  message = json1['message']
  answer=chatbot_final.chat(message)
  json1['answer'] = answer
  json1['bot']='AdhocBot'
  print( 'recived my event: ' + str(json1 ))
  socketio.emit( 'my response', json1, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )