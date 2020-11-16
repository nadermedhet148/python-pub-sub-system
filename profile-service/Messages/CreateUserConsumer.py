from .consumer import consumer
from Models.Profile import Profile
from Models.manger import session_factory
import json
import random
import string


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def create_user_profile(ch, method, properties, body):
    session = session_factory()
    user = json.loads(str(body, 'utf-8'))
    profile = Profile(get_random_string(user['id']), user['id'])
    session.add(profile)
    session.commit()
    session.close()


def create_user_consumer():
    consumer(channel_name="user_created", callback=create_user_profile)
