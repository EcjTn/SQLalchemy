from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from database import Base



class PlayerBase(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    password = Column(String, index=True)
