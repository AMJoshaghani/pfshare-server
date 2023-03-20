from flask import Blueprint, request, abort, jsonify
import os
from flask import send_file
from urllib.parse import unquote
import random
import sqlite3
from functions import execute_db

api = Blueprint("api", __name__, url_prefix='/api/')


@api.route('/')
def api_home():
    return "API URLS INDEX"


@api.route('/download/')  # <path:filename>
def download_file():
    filename = request.args.get('filename')
    if filename:
        path = os.path.join('/', unquote(filename))
        return send_file(path, as_attachment=True)
    else:
        return abort(404)


@api.route('/upload/', methods=['POST'])
def upload_file():
    temporary_dir = os.environ['pfshare-temp']
    file = request.files.get('file')
    if file:
        db = sqlite3.connect(temporary_dir + "/database.db")
        fname = str(random.randint(1000, 9999)) + file.filename
        fpath = temporary_dir + "/" + fname
        file.save(open(fpath, 'w+b'))
        execute_db(db, fname, fpath)
        db.close()
        return jsonify({
            'success': 1
        })
    else:
        return jsonify({
            'success': 0,
            'err': 'file not specified...'
        })
