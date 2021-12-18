from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from today import db
from today.forms import UserCreateForm, UserLoginForm
from today.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

#회원가입#

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(user_id=form.user_id.data).first() 
        if not user:
            user = User(user_id=form.user_id.data,
                    password=generate_password_hash(form.password1.data),
                    name=form.name.data,
                    address=form.address.data,
                    detail_address=form.detail_address.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

#로그인#

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(user_id=form.user_id.data).first()
        if not user:
            form.user_id.errors.append("존재하지 않는 사용자입니다.")
            error=1
            return render_template('auth/login.html', form=form)
        elif not check_password_hash(user.password, form.password.data):
            form.password.errors.append("비밀번호가 올바르지 않습니다.")
            error=2
            return render_template('auth/login.html', form=form)
        if error is None:
            session.clear()
            session['user_id']= user.id
            return redirect(url_for('main.index'))
    return render_template('auth/login.html', form=form)

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)
