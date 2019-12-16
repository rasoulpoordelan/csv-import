from flask import Flask,request,render_template
from jinja2 import Template
from flask_sqlalchemy import SQLAlchemy
import datetime
import logging 
import sys

db_name='data.db' 
if len(sys.argv) > 1 :
    db_name= sys.argv[1]

port='8080' 
if len(sys.argv) > 2 :
    db_name= sys.argv[2]

app = Flask(__name__,template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
db = SQLAlchemy(app)

def paginate(total,page,size,pagenation_size):
    total_page=(total//size)
    start=0
    end=0
    if total_page <= pagenation_size:
        start,end=1,total_page
    elif total_page > pagenation_size:
        if page == 1 :
            start,end=1,pagenation_size
        elif page+pagenation_size > total_page:
            start,end=page-(pagenation_size -(total_page-page) ) ,total_page  
        else:
            start,end = page,page+pagenation_size 
    return {
        "pages":[(i,size) for i in range(start,end+1)],
        "page":page,
        "size":size,
        "has_next":True if page < total_page else False,
        "has_previous":True if page != 1 else False
    }


class LogData(db.Model):
    __tablename__ = "log"
    iid = db.Column(db.Integer, primary_key=True,autoincrement=True)
    timestamp = db.Column(db.DateTime)
    msg = db.Column(db.String(250))
    

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    temperature = db.Column(db.DECIMAL)
    duration = db.Column(db.Interval)

class DBHandler(logging.StreamHandler):
    def __init__(self):
        logging.StreamHandler.__init__(self)

    def emit(self, record):
        msg = self.format(record)
        db.session.add(LogData(timestamp=datetime.datetime.now(),msg=msg))
        db.session.commit()

@app.before_request
def start_timer():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)
    path=request.path
    app.logger.info(f'request address => {path} ip => {ip} host => {host} args => {args} ') 
    

@app.route('/')
def index():
    
    page = int( request.args.get('page',1))
    size = int( request.args.get('size',50))
    
    skip=(int(page)-1) * int(size)
    out_data=Data.query.limit(size).offset(skip).all()
    total=Data.query.count()
    
    return render_template('show_data.html', my_data=out_data, pagination=paginate(total,page,size,10))

if __name__ == '__main__':
    db.create_all()
    handler = DBHandler()
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info(f'Start App Port {port}')

    app.run(debug=True,port=port)