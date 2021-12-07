from flask import Blueprint, render_template

from today.models import User

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/')
def form():
    return "로그인 화면"
