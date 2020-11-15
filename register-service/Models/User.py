from sqlalchemy import Column, String, Date, Integer, Numeric

from .manger import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def to_string(self):
        return f'name : {self.name}  id : {self.id}'
