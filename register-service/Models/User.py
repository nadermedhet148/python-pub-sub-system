from sqlalchemy import Column, String, Date, Integer, Numeric
import json
from .manger import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def to_json_string(self):
        return json.dumps({
            "id": self.id,
            "name": self.name
        })
