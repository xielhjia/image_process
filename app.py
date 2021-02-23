from flask import Flask, render_template, request, send_file
from flask_sockets import Sockets
import datetime
import time
import random
import base64
import io

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:

        now = datetime.datetime.now().isoformat() + 'Z'
        ws.send(now)  #发送数据
        # time.sleep(1)



@app.route('/')
# def hello():
#     return 'Hello World!'
def index():
    # return render_template('index.html')
    return app.send_static_file('index.html')

@app.route('/img/<iid>')
def get_image(iid):
    print('get image:', iid)
    return send_file('static/img/'+iid, mimetype='image/png')

def get_image(image_path):
    img = file(image_path)
    resp = Response(img, mimetype="image/png")
    return resp


if __name__ == "__main__":
    # from gevent import pywsgi
    # from geventwebsocket.handler import WebSocketHandler
    # server = pywsgi.WSGIServer(('127.0.0.1', 5001), app, handler_class=WebSocketHandler)
    # print('server start')
    # server.serve_forever()

    app.run(host='127.0.0.1', port=8080, debug=True)


