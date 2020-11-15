from flask import Blueprint, request

from Models.User import User
from Models.manger import session_factory

user_resource = Blueprint('users', __name__)


@user_resource.route('/', methods=['POST'])
def api_root():
    if request.method == 'POST' and request.files['image']:
        try:
            session = session_factory()
            user = User("John Doe")
            session.add(user)
            session.commit()
            session.close()
            return user.to_string()
        except Exception as ex:
            return ex

    else:
        return "Where is the image?"
