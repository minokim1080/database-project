from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, FloatField, BooleanField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo

class UserCreateForm(FlaskForm):
    user_id = StringField('아이디', validators=[DataRequired()])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    gender = StringField('성별', validators=[DataRequired()])
    age = FloatField('나이', validators=[DataRequired()])
    height = FloatField('키(cm)', validators=[DataRequired()])
    weight = FloatField('체중(kg)', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    user_id = StringField('ID', validators=[DataRequired('아이디는 필수 입력 항목입니다.')])
    password = PasswordField('PW', validators=[DataRequired('비밀번호는 필수 입력 항목입니다.')])

class ColorForm(FlaskForm):
    color = StringField('컬러', validators=[DataRequired()])
