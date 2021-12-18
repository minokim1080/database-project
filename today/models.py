from today import db

import datetime


## 회원정보. 아이디 비밀번호,이름, 주소, 상세주소로 이루어져 있음 ##
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    detail_address = db.Column(db.String(255), nullable=False)


## 옷 정보, 옷 이름, 종류,, 이미지주소, 가격으로 이루어져 있음 ##
class Cloth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    cloth_type = db.Column(db.String(255), nullable=False)
    img = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)

# 배송지 정보, 유저 정보와 주소지 정보를 담고 있음. 외래키로 설정할 때 오류가 발생하여 어쩔 수 없이 외래키 없이 진행하였습니다. #
class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    detail_address = db.Column(db.String(255), nullable=False)


# 장바구니. 유저정보와 옷 정보를 담고 있음. 외래키로 설정할 때 오류가 발생하여 어쩔 수 없이 외래키 없이 진행하였습니다. #
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cloth_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)


# 주문정보. 사용자들의 구매내역을 담고 있다. result는 배송여부를 반영한다. 외래키로 설정할 때 오류가 발생하여 어쩔 수 없이 외래키 없이 진행하였습니다. #
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    cloth_id = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String(255), nullable=False)

