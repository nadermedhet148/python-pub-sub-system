from flask import Blueprint, request

from Models.User import User
from Models.manger import session_factory
from Messages.publish import publish

user_resource = Blueprint('users', __name__)


@user_resource.route('/', methods=['POST'])
def api_root():
    print(request.form)
    if request.method == 'POST' and request.form:
        try:
            session = session_factory()
            user = User(request.form["name"])
            session.add(user)
            session.commit()
            session.close()
            publish('user_created', user.to_json_string())
            return user.to_json_string()
        except Exception as ex:
            return ex

    else:
        return "Where is the image?"
