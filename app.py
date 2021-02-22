from flask import Flask, render_template, request
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
        time.sleep(1)



@app.route('/')
# def hello():
#     return 'Hello World!'
def index():
    return render_template('index.html')

@app.route('/img/<int:pid>.png')
def get_image(pid):
    image_binary = get_image('./img/1.png')
    # response = make_response(image_binary)
    # response.headers.set('Content-Type', 'image/jpeg')
    # response.headers.set(
    #     'Content-Disposition', 'attachment', filename='%s.jpg' % pid)
    return image_binary
    # return '1111111'

def get_image(image_path):
    img = Image.open(image_path, mode='r')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    encoded_img = base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')
    return encoded_img


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()
