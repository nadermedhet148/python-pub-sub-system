from sqlalchemy import Column, String, Date, Integer, Numeric
import json
from .manger import Base


class AddressBook(Base):
    __tablename__ = 'address_book'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)

    def __init__(self, user_id):
        self.user_id = user_id

    def to_json_string(self):
        return json.dumps({
            "id": self.id,
            "user_id": self.user_id,
        })
