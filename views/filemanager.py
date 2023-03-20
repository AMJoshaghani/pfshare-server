from flask import Blueprint, render_template
from functions import icon, file_size
import os
import time

filemanager = Blueprint("filemanager", __name__, url_prefix='/filemanager/')


@filemanager.route('/')
def fm_home():
    return file_path("/")


@filemanager.route('/<path:dirpath>')
def file_path(dirpath):
    dirname = dirpath if dirpath.startswith("/") else '/' + dirpath + '/'
    dirfiles = os.listdir(dirname)
    fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)
    dirs = ['..']
    files = {}
    for file in fullpaths:
        if os.path.isdir(file):
            dirs.append(file)

        if os.path.isfile(file):
            filename, file_extension = os.path.splitext(file)
            files[file] = {
                "name": os.path.basename(file),
                "extension": file_extension,
                "info": {
                    "path": file,
                    "access time": time.ctime(os.path.getatime(file)),
                    "modify time": time.ctime(os.path.getmtime(file)),
                    "change time": time.ctime(os.path.getctime(file)),
                    "size": file_size(file)
                }
            }

    return render_template('filemanager.html', files=files, dirs=dirs, icon=icon, current_dir=dirname)
