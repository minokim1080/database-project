from flask import Blueprint, url_for, render_template, flash, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

import random

from today import db
from today.forms import UserCreateForm, UserLoginForm
from today.models import User, Cloth

bp = Blueprint('result', __name__, url_prefix='/result')

@bp.route('/result/', methods=('GET', 'POST'))
def result():
    red = Cloth.query.filter(Cloth.color=='빨강').all()
    orange = Cloth.query.filter(Cloth.color=='주황').all()
    yellow = Cloth.query.filter(Cloth.color=='노랑').all()
    green = Cloth.query.filter(Cloth.color=='초록').all()
    blue = Cloth.query.filter(Cloth.color=='파랑').all()
    purple = Cloth.query.filter(Cloth.color=='보라').all()
    black = Cloth.query.filter(Cloth.color=='검정').all()
    grey = Cloth.query.filter(Cloth.color=='회색').all()
    white = Cloth.query.filter(Cloth.color=='하양').all()
    beige = Cloth.query.filter(Cloth.color=='베이지').all()
    pink = Cloth.query.filter(Cloth.color=='분홍').all()
    navy = Cloth.query.filter(Cloth.color=='남색').all()
    brown = Cloth.query.filter(Cloth.color=='갈색').all()
    top_box =[]
    top_name= []
    top_url=[]
    bottom_box =[]
    bottom_name=[]
    bottom_url=[]
    outer_box =[]
    outer_name=[]
    outer_url=[]
    if session['bmi'] >=23.5 and session['gender'] == "남자" :
        if session['color'] == "회색":
            box = beige + white + black + green + grey
            for i in range(0,len(box)):
                if box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_box = top_box + [img]
                    top_name = top_name + [name]
                    top_url = top_url + [url]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]
                    bottom_url = bottom_url + [url]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]
                    outer_url = outer_url + [url]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            
            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)
        
        elif session['color'] =="베이지":
            box = pink + grey + green + red + orange + brown + white + beige
            for i in range(0,len(box)):
                if box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url + [url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url + [url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="검정":
            box = grey + brown + green + red + blue + navy+ white + black
            for i in range(0, len(box)):
                if box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="남색":
            box = black + beige + blue + yellow
            for i in range(0, len(box)):
                if box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="파랑":
            box = navy + blue + black + beige + pink + white + grey + yellow
            for i in range(0,len(box)):
                if box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="갈색":
            box = beige + navy + green
            for i in range(0, len(box)):
                if box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        else:
            box = Cloth.query.all()
            for i in range(0,len(box)):
                if box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)


    elif session['bmi'] < 23.5 and session['gender'] == "남자" :
        if session['color'] == "회색":
            box = beige + white + black + green + grey
            for i in range(0,len(box)):
                if box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="베이지":
            box = pink + grey + green + red + orange + brown + white + beige
            for i in range(0,len(box)):
                if box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="검정":
            box = grey + brown + green + red + blue + navy+ white + black
            for i in range(0, len(box)):
                if box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="남색":
            box = black + beige + blue + yellow
            for i in range(0, len(box)):
                if box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="파랑":
            box = navy + blue + black + beige + pink + white + grey + yellow
            for i in range(0,len(box)):
                if box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="갈색":
            box = beige + navy + green
            for i in range(0, len(box)):
                if box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        else:
            box = Cloth.query.all()
            for i in range(0,len(box)):
                if box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '남자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

    elif session['bmi'] >=23.5 and session['gender'] == "여자" :
        if session['color'] == "회색":
            box = beige + white + black + green + grey
            for i in range(0,len(box)):
                if box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="베이지":
            box = pink + grey + green + red + orange + brown + white + beige
            for i in range(0,len(box)):
                if box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="검정":
            box = grey + brown + green + red + blue + navy+ white + black
            for i in range(0, len(box)):
                if box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="남색":
            box = black + beige + blue + yellow
            for i in range(0, len(box)):
                if box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="파랑":
            box = navy + blue + black + beige + pink + white + grey + yellow
            for i in range(0,len(box)):
                if box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="하양":
            box = pink + green + blue + yellow + black
            for i in range(0, len(box)):
                if box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="초록":
            box = grey+ beige + white
            for i in range(0, len(box)):
                if box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        else:
            box = Cloth.query.all()
            for i in range(0,len(box)):
                if box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='오버' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

    elif session['bmi'] < 23.5 and session['gender'] == "여자" :
        if session['color'] == "회색":
            box = beige + white + black + green + grey
            for i in range(0,len(box)):
                if box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="베이지":
            box = pink + grey + green + red + orange + brown + white + beige
            for i in range(0,len(box)):
                if box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="검정":
            box = grey + brown + green + red + blue + navy+ white + black
            for i in range(0, len(box)):
                if box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="남색":
            box = black + beige + blue + yellow
            for i in range(0, len(box)):
                if box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="파랑":
            box = navy + blue + black + beige + pink + white + grey + yellow
            for i in range(0,len(box)):
                if box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="하양":
            box = pink + green + blue + yellow + black
            for i in range(0, len(box)):
                if box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        elif session['color'] =="초록":
            box = grey+ beige + white
            for i in range(0, len(box)):
                if box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)

        else:
            box = Cloth.query.all()
            for i in range(0,len(box)):
                if box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '상의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    top_url = top_url +[url]
                    top_box = top_box + [img]
                    top_name = top_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '하의':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    bottom_url = bottom_url +[url]
                    bottom_box = bottom_box + [img]
                    bottom_name = bottom_name + [name]

                elif box[i].gender == '여자' and box[i].fit =='레귤러' and box[i].cloth_type == '아우터':
                    name = box[i].classification
                    img = box[i].img
                    url = box[i].url
                    outer_url = outer_url +[url]
                    outer_box = outer_box + [img]
                    outer_name = outer_name + [name]

            top_item = random.randrange(0,len(top_box))
            bottom_item = random.randrange(0,len(bottom_box))
            outer_item = random.randrange(0,len(outer_box))
            top = top_box[top_item]
            bottom = bottom_box[bottom_item]
            outer = outer_box[outer_item]
            session['top'] = top
            session['bottom'] = bottom
            session['outer'] = outer
            session['top_name'] = top_name[top_item]
            session['bottom_name'] = bottom_name[bottom_item]
            session['outer_item'] = outer_name[outer_item]
            session['top_url'] = top_url[top_item]
            session['bottom_url'] = bottom_url[bottom_item]
            session['outer_url'] = outer_url[outer_item]

            return render_template('result/result.html', top=top, bottom=bottom, outer=outer)


@bp.route('/final/', methods=('GET', 'POST'))
def final():
    top = session['top']
    bottom = session['bottom']
    outer = session['outer']
    top_name = session['top_name']
    bottom_name = session['bottom_name']
    outer_name = session['outer_item']
    top_url= session['top_url']
    bottom_url = session['bottom_url']
    outer_url = session['outer_url']

    return render_template('result/final.html', top=top, bottom=bottom, outer=outer, top_name=top_name, bottom_name=bottom_name, outer_name=outer_name, top_url=top_url, bottom_url=bottom_url, outer_url=outer_url)
