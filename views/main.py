from flask import Blueprint, render_template

main = Blueprint("main", __name__, url_prefix='/')


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/favicon.ico')
def fav():
    return ''
