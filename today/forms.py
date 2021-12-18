from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, FloatField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo


#회원가입을 받기 위한 폼 양식#
class UserCreateForm(FlaskForm):
    user_id = StringField('아이디', validators=[DataRequired()])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    name = StringField('이름', validators=[DataRequired()])
    address = StringField('주소', validators=[DataRequired()])
    detail_address = StringField('상세주소', validators=[DataRequired()])

#로그인 폼 양식#
class UserLoginForm(FlaskForm):
    user_id = StringField('ID', validators=[DataRequired('아이디는 필수 입력 항목입니다.')])
    password = PasswordField('PW', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.')])

# 배송지를 입력받는 폼 양식#
class DeliveryForm(FlaskForm):
    user_name = StringField('이름', validators=[DataRequired()])
    address = StringField('주소', validators=[DataRequired()])
    detail_address = StringField('상세주소', validators=[DataRequired()])
