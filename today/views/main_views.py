from flask import Blueprint, render_template, flash, request
from flask import url_for
from werkzeug.utils import redirect

from today import db
from today.forms import UserCreateForm
from today.models import User, Cloth

bp = Blueprint('main', __name__, url_prefix='/')

#메인화면#

@bp.route('/')
def index():
    return render_template('main.html')


