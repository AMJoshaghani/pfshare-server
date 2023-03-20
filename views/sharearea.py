from flask import Blueprint, render_template
import sqlite3
from functions import get_files_db, file_size
import os

sharearea = Blueprint("sharearea", __name__, url_prefix="/sharearea/")


@sharearea.route("/")
def sharearea_home():
    db = sqlite3.connect(os.environ['pfshare-temp'] + "/database.db")
    files = get_files_db(db)
    return render_template("sharearea.html", files=files, tempdir=os.environ['pfshare-temp'], s=file_size)
