from flask import Flask, request, render_template
import logging
import sys
from share.models import Data
from share import repo as db
from share import util
from share.db_log_handler import DBHandler

db_name = "data.db"
if len(sys.argv) > 1:
    db_name = sys.argv[1]

port = "8080"
if len(sys.argv) > 2:
    db_name = sys.argv[2]

app = Flask(__name__, template_folder="templates")

engine = db.connect(db_name)
session = db.get_session(engine)


@app.before_request
def start_timer():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    host = request.host.split(":", 1)[0]
    args = dict(request.args)
    path = request.path
    app.logger.info(
        f"request address => {path} ip => {ip} host => {host} args => {args}"
    )


@app.route("/")
def index():
    page = int(request.args.get("page", 1))
    size = int(request.args.get("size", 50))

    skip = (int(page) - 1) * int(size)
    out_data = session.query(Data).limit(size).offset(skip).all()
    total = session.query(Data).count()

    return render_template(
        "show_data.html",
        my_data=out_data,
        pagination=util.paginate(total, page, size, 10),
    )


if __name__ == "__main__":
    handler = DBHandler(session)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info(f"Start App Port {port}")

    app.run(debug=True, port=port)
