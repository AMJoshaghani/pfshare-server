from app import app
import sys
import os
import tempfile
import sqlite3
from functions import initialize_db

if __name__ == "__main__":
    host = sys.argv[1]  # ex. 0.0.0.0
    port = sys.argv[2]  # ex. 5000
    debug = True if len(sys.argv) > 3 and sys.argv[3] == "true" or "1" or "True" else False  # ex. true
    temporary_dir = tempfile.mkdtemp(prefix="pfshare-")
    os.environ["pfshare-temp"] = temporary_dir
    initialize_db(sqlite3.connect(temporary_dir + "/database.db"))
    app.run(host=host, port=port, debug=debug)
