from flask import Flask
from views import api, main, filemanager, sharearea

app = Flask(__name__)


app.register_blueprint(main.main, urlprefix="/")
app.register_blueprint(api.api, urlprefix="/api/")
app.register_blueprint(filemanager.filemanager, urlprefix="/filemanager/")
app.register_blueprint(sharearea.sharearea, urlprefix="/sharearea/")

if __name__ == '__main__':
    print("please RUN run.py first...")
    exit(1)
