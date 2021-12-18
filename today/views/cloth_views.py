from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

from today import db
from today.models import User,Cloth

bp = Blueprint('cloth', __name__, url_prefix='/cloth')


## 상의 화면 ##

@bp.route('/top/', methods=('GET', 'POST'))
def top():
    top = Cloth.query.filter(Cloth.cloth_type =='상의').all()
    top_img = []
    top_price = []
    top_name = []
    top_id = []
    for i in range(0,len(top)):
        top_img = top_img + [top[i].img]
        top_price = top_price + [top[i].price]
        top_name = top_name + [top[i].name]
        top_id = top_id + [top[i].id]

    return render_template('topPage.html', img=top_img, price=top_price, name=top_name, cloth_id=top_id)

@bp.route('/bottom/', methods=('GET', 'POST'))
def bottom():
    bottom = Cloth.query.filter(Cloth.cloth_type =='하의').all()
    bottom_img = []
    bottom_price = []
    bottom_name = []
    bottom_id = []
    for i in range(0,len(bottom)):
        bottom_img = bottom_img + [bottom[i].img]
        bottom_price = bottom_price + [bottom[i].price]
        bottom_name = bottom_name + [bottom[i].name]
        bottom_id = bottom_id + [bottom[i].id]

    return render_template('bottomPage.html', img=bottom_img, price=bottom_price, name=bottom_name, cloth_id=bottom_id)


@bp.route('/outer/', methods=('GET', 'POST'))
def outer():
    outer = Cloth.query.filter(Cloth.cloth_type =='아우터').all()
    outer_img = []
    outer_price = []
    outer_name = []
    outer_id = []
    for i in range(0,len(outer)):
        outer_img = outer_img + [outer[i].img]
        outer_price = outer_price + [outer[i].price]
        outer_name = outer_name + [outer[i].name]
        outer_id = outer_id + [outer[i].id]

    return render_template('outerPage.html', img=outer_img, price=outer_price, name=outer_name, cloth_id=outer_id)

