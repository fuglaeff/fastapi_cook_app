from sqlalchemy import Boolean, Column, Enum, Integer, String

from ..db import Base, engine
from ..recipies.schemas import Rating


class UserSQL(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    hashed_pwd = Column(String)
    is_activ = Column(Boolean)


class ProfileSQL(Base):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    cooking_level = Column(Enum(Rating))
    email = Column(String)


Base.metadata.create_all(engine)
