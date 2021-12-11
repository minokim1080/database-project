from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from today import db
from today.forms import ColorForm
from today.models import User

bp = Blueprint('select', __name__, url_prefix='/select')

@bp.route('/selection/', methods=('GET', 'POST'))
def selection():
    return render_template('select/selection.html')

@bp.route('/color/', methods=('GET', 'POST'))
def color():
    form = ColorForm()
    if session['gender'] == '남자' and request.method == 'GET':
        return render_template('select/colorMale.html', form=form)
    elif session['gender'] == '여자' and request.method == 'GET':
        return render_template('select/colorFemale.html', form=form)
    elif request.method =='POST' and form.validate_on_submit():
        session['color'] = form.color.data
        return redirect(url_for('result.result'))
    else:
        flash('색을 선택해야 합니다')


@bp.route('/date/', methods=('GET', 'POST'))
def date():
    return render_template('select/tempCal.html')

@bp.route('/location/', methods=('GET', 'POST'))
def location():
    return render_template('select/tempLoc.html')
