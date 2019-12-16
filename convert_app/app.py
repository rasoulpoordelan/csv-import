import sys
import util as ut
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
import datetime
import csv
from decimal import Decimal

file_name='data.csv'
if len( sys.argv) > 1 :
     file_name = sys.argv[1]

print(len(sys.argv))

db_name='data.db' 
if len(sys.argv) > 2 :
    db_name= sys.argv[2]


engine = create_engine(f'sqlite:///{db_name}')
Base = declarative_base()

class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    temperature = Column(DECIMAL)
    duration = Column(Interval)

Data.__table__.create(bind=engine, checkfirst=True)

Session = sessionmaker(bind=engine)
session = Session()

with open(file_name, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        data = Data(id = row["id"],
                    timestamp = datetime.datetime.now(),
                    temperature = Decimal(row["temperature"]) ,
                    duration= ut.convert_string_to_timedelta(row["duration"]))
        session.add(data)
        session.commit()



