from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from today import db
from today.models import User

bp = Blueprint('select', __name__, url_prefix='/select')

@bp.route('/selection/', methods=('GET', 'POST'))
def selection():
    return render_template('select/selection.html')

@bp.route('/color/', methods=('GET', 'POST'))
def color():
    return render_template('select/selectColor.html')

@bp.route('/date/', methods=('GET', 'POST'))
def date():
    return render_template('select/tempCal.html')

@bp.route('/location/', methods=('GET', 'POST'))
def location():
    return render_template('select/tempLoc.html')
