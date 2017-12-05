
"""
视图模型
"""

from flask import render_template, Blueprint, redirect, url_for, flash, g
from app import login_manger
from form import Login_Form, Register_Form
from model import Users
from flask_login import login_user, logout_user, login_required, current_user
from app import db, app


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
def index():
    form = Login_Form()
    return render_template('index.html')


@app.route('/index')
def l_index():
    form = Login_Form()
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is not None and user.password == form.password.data:
            login_user(user)
            # flash('登录成功')
            return render_template('vip.html', username=form.username.data)
        else:
            # flash('用户或密码错误')
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)


# 用户登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    # flash('你已退出登录')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    print('ok')
    form = Register_Form()
    if form.validate_on_submit():
        user = Users(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('注册成功')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/vip')
@login_required
def vip():
    return render_template('vip.html', username=g.user)
