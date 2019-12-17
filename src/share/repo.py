from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from share.models import Data, LogData


def connect(db_name):
    engine = create_engine(f"sqlite:///{db_name}")
    __create_table_not_exist(engine)
    return engine


def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


def __create_table_not_exist(engine):
    Data.__table__.create(bind=engine, checkfirst=True)
    LogData.__table__.create(bind=engine, checkfirst=True)
