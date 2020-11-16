from sqlalchemy import Column, String, Date, Integer, Numeric
import json
from .manger import Base


class Profile(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    account_number = Column(String)


    def __init__(self, account_number, user_id):
        self.user_id = user_id
        self.account_number = account_number

    def to_json_string(self):
        return json.dumps({
            "id": self.id,
            "user_id": self.user_id,
            "account_number": self.account_number
        })
