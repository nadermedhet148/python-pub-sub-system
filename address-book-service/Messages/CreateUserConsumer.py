from .consumer import consumer
from Models.AddressBook import AddressBook
from Models.manger import session_factory
import json


def create_user_address_book(ch, method, properties, body):
    session = session_factory()
    user = json.loads(str(body, 'utf-8'))
    address_book = AddressBook(user['id'])
    session.add(address_book)
    session.commit()
    session.close()


def create_user_consumer():
    consumer(channel_name="user_created", callback=create_user_address_book)
