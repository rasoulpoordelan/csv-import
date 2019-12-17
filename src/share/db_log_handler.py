import datetime
import logging
from share.models import LogData


class DBHandler(logging.StreamHandler):
    def __init__(self, session):
        logging.StreamHandler.__init__(self)
        self.session = session

    def emit(self, record):
        msg = self.format(record)
        self.session.add(LogData(timestamp=datetime.datetime.now(), msg=msg))
        self.session.commit()
