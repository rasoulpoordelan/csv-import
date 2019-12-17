from sqlalchemy import Column, Integer, DateTime, DECIMAL, Interval, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    temperature = Column(DECIMAL)
    duration = Column(Interval)


class LogData(Base):
    __tablename__ = "log"
    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime)
    msg = Column(String(250))
