from flask import Flask, url_for, send_from_directory, request

from resources.create import user_resource


app = Flask(__name__)
app.register_blueprint(user_resource)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
