from sqlalchemy import Sequence, Column, Integer, String
from extensions import Base


class Person(Base):
    __tablename__ = 'person'
    __versioned__ = {}  # <- IMPORTANT!
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))
