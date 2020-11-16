from flask import Flask, url_for, send_from_directory, request
import logging
import threading
import time

from Messages.CreateUserConsumer import create_user_consumer

app = Flask(__name__)


def start_app():
    app.run(host='0.0.0.0', port=5200, debug=False)


if __name__ == '__main__':
    t1 = threading.Thread(target=create_user_consumer)
    t2 = threading.Thread(target=start_app)
    t1.start()
    t2.start()
