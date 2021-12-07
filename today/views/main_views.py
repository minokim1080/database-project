from flask import Blueprint, render_template, flash, request
from flask import url_for
from werkzeug.utils import redirect

from today import db
from today.forms import UserCreateForm
from today.models import User

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello,Pybo!'

@bp.route('/')
def index():
    return render_template('main.html')


