import sys
import datetime
import csv
from decimal import Decimal
from share.models import Data
from share import repo as db
from share import util as ut

file_name = "data.csv"
if len(sys.argv) > 1:
    file_name = sys.argv[1]

db_name = "data.db"
if len(sys.argv) > 2:
    db_name = sys.argv[2]

engine = db.connect(db_name)
session = db.get_session(engine)

with open(file_name, mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        data = Data(
            id=row["id"],
            timestamp=datetime.datetime.strptime(
                row["timestamp"], "%Y-%m-%d %H:%M:%S.%f"
            ),
            temperature=Decimal(row["temperature"]),
            duration=ut.convert_string_to_timedelta(row["duration"]),
        )
        session.add(data)
        session.commit()

print("import finish")

