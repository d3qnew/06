

from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required
from flask_wtf import FlaskForm


# 登录表单
class Login_Form(FlaskForm):
    username = StringField('用户名', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('登录')


# 注册表单
class Register_Form(FlaskForm):
    username = StringField('用户名', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('注册')
