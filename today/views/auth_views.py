from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from today import db
from today.forms import UserCreateForm, UserLoginForm
from today.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(user_id=form.user_id.data).first() 
        if not user:
            user = User(user_id=form.user_id.data,
                    password=generate_password_hash(form.password1.data),
                    gender=form.gender.data,
                    age=form.age.data,
                    height=form.height.data,
                    weight=form.weight.data,
                    bmi=float(form.weight.data/((form.height.data**2)/10000)))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

@bp.route('/login/', methods=('GET', 'POST'))
def login():
    #form = UserLoginForm()
    # if request.method == 'POST' and form.validate_on_submit():
    #     userid = form['user_id'].data
    #     userpw = form['password'].data
    #     user = User.query.filter(User.user_id == userid).first()
    #     error = None
    #     if not user:
    #         form.user_id.errors.append("*존재하지 않는 사용자입니다.")
    #         error = 1
    #         return render_template('auth/login.html', form=form)
    #     elif not check_password_hash(user.password, userpw):
    #         form.password.errors.append("*비밀번호가 올바르지 않습니다.")
    #         error = 2
    #         return render_template('auth/login.html', form=form)
    #     if error is None:
    #         session.clear()
    #         session['user_id']= user.id
    #         return redirect(url_for('select.selection'))
    # return render_template('auth/login.html', form=form)

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
            return redirect(url_for('select.selection'))
    return render_template('auth/login.html', form=form)
