from datetime import datetime
from flask import render_template, Blueprint, redirect, url_for, flash, g, jsonify, request, abort
from app import login_manger
from form import Login_Form, Register_Form
from model import Users
from flask_login import login_user, logout_user, login_required, current_user
from txt import txt
from app import db, app


@app.before_request
def before_request():
    g.user = current_user
    # print(g.user)


@app.route('/')
@app.route('/home')
@app.route('/index')
def l_index():
    form = Login_Form()
    return render_template(
        'index.html',
        title='首页',
        year=datetime.now().year,

    )


@app.route('/xtest', methods=['GET', 'POST'])
def xtest():
    p = request.form['text']
    print(p)
    return render_template(
        'xtest.html',
        title='xtest',
        year=datetime.now().year,

    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is not None and user.password == form.password.data:
            login_user(user)
            # flash('登录成功')
            return render_template('vip.html', username=form.username.data, mss="alert('登录成功');")
        else:
            # flash('用户或密码错误')
            return render_template('login.html', form=form, mss='用户或密码错误')
    else:
        return render_template('login.html', form=form)


# 用户登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    # flash('你已退出登录')
    return redirect(url_for('index'))


# 注册
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     print('ok')
#     form = Register_Form()
#     if form.validate_on_submit():
#         user = Users(username=form.username.data, password=form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         # flash('注册成功')
#         return redirect(url_for('index'))
#     return render_template('register.html', form=form)


@app.route('/vip')
@login_required
def vip():
    return render_template('vip.html', username=g.user)


@app.route('/story')
def story():
    return render_template(
        'story.html',
        title='品牌故事',
        year=datetime.now().year,

    )


# 新闻
@app.route('/news', methods=['GET', 'POST'])
def news():
    newsls = []
    for i in range(len(txt['news'])):
        newsls.append(txt['news'][i]['id'])
    try:
        id = request.args.get('id', '')  # 获取GET参数，没有参数就赋值 0
    except ValueError:
        abort(404)  # 返回 404

    if (id != '' and id in newsls):
        return render_template(
            'newstopic.html',
            title='品牌动态',
            year=datetime.now().year,
            txt=txt['news'][int(id)]
        )
    else:
        return render_template(
            'news.html',
            title='品牌动态',
            year=datetime.now().year,
            txt=txt['news']

        )


# 加入我们
@app.route('/joinus')
def joinus():
    return render_template(
        'joinus.html',
        title='joinus',
        zhaopin = txt['joinus']['zhaopin'],
        year=datetime.now().year
    )


# 权威认证
@app.route('/Certification')
def certification():
    return render_template(
        'certification.html',
        title='Certification',
        year=datetime.now().year
    )


# 经销商地图
@app.route('/agency')
def agency():
    return render_template(
        'agency.html',
        title='agency',
        year=datetime.now().year,
        mapdate=txt['agency']
    )


# 保温
@app.route('/baowen')
def baowen():
    return render_template(
        'baowen.html',
        title='baowen',
        year=datetime.now().year
    )

# 静音
@app.route('/jingyin')
def jingyin():
    return render_template(
        'jingyin.html',
        title='jingyin',
        year=datetime.now().year
    )


# 密封
@app.route('/mifeng')
def mifeng():
    return render_template(
        'mifeng.html',
        title='mifeng',
        year=datetime.now().year
    )

#售后
@app.route('/fuwu')
def shouhou():
    return render_template(
        'fuwu.html',
        title='fuwu',
        year=datetime.now().year
    )

#问题
@app.route('/wenti')
def wenti():
    return render_template(
        'wenti.html',
        title='wenti',
        year=datetime.now().year
    )

#极简生活
@app.route('/jijianshenghuo')
def jijianshenghuo():
    return render_template(
        'jijianshenghuo.html',
        title='jijianshenghuo',
        year=datetime.now().year
    )

#轻奢品质
@app.route('/qingshepinzhi')
def qingshepinzhi():
    return render_template(
        'qingshepinzhi.html',
        title='qingshepinzhi',
        year=datetime.now().year
    )

#传世至尊
@app.route('/chuanshizhizun')
def chuanshizhizun():
    return render_template(
        'chuanshizhizun.html',
        title='chuanshizhizun',
        year=datetime.now().year
    )

#传世至尊
@app.route('/shejishi')
def shejishi():
    return render_template(
        'shejishi.html',
        title='shejishi',
        txt=txt['shejishi'],
        year=datetime.now().year
    )