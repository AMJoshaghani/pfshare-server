import json
import os


def file_size(fpath):
    return str(round(os.path.getsize(fpath), ndigits=100)) + " bytes" if os.path.getsize(fpath) < 100 else \
           str(round(os.path.getsize(fpath) / 100, ndigits=100)) + " KB" if 1000*1000 > os.path.getsize(fpath) > 100 else \
           str(round(os.path.getsize(fpath) / (1000 * 1000), ndigits=100)) + " MB"


def icon(ft: str):
    filetype = ft.lower()
    root_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root_path, "static/types.json")) as data:
        types = json.loads(data.read())

    if filetype in types.keys():
        return types[filetype]
    else:
        path = ''
        for i in types.keys():
            if filetype in types[i] and type(types[i]) is not str:
                path = i
        if path == '':
            return types['undef']
        else:
            return path


def initialize_db(db):
    db.execute("CREATE TABLE `files` (filename TEXT, filepath TEXT);")
    db.commit()
    return True


def execute_db(db, name, path):
    db.execute("INSERT INTO `files` VALUES ('%s', '%s')" % (name, path))
    db.commit()
    return True


def get_files_db(db):
    return db.execute("SELECT * FROM `files`").fetchall()
