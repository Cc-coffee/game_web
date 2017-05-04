# -*- coding: utf-8 -*-
from django.http import request
from flask_moment import Moment
from datetime import datetime
from flask import *
from model import *
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)
# 时间
Moment(app)
# flash
app.secret_key = 'some_secret'


##################################################################
# md5加密
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()


##################################################################

# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/test')
def test():
    return render_template('userinfo.html')


# 主页
@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


# 自定义错误页面
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404
# @app.errorhandler(500)
# def internal_server_error(e):
#     eturn render_template('500.html'), 500


# 登录请求
@app.route('/login', methods=['POST', 'GET'])
def login():
    #  flash(u'登录成功，欢迎回来！', 'success')
    #    flash(u'登录信息', 'info')
    #  flash(u'登录警告', 'warning')
    if request.method == 'POST':
        try:
            uemail_1 = request.form['email']
            uemail_2 = User.query.filter_by(email=uemail_1).first().email
            upsd_1 = md5(request.form['password'])
            upsd_2 = User.query.filter_by(email=uemail_1).first().password
        except:
            flash(u'用户名密码错', 'danger')
            # render_template("login.html")
        else:
            if uemail_1 == uemail_2 and upsd_1 == upsd_2:
                return redirect(url_for('test'))
            else:
                flash(u'用户名密码错', 'danger')
                #  render_template("login.html")
    return render_template("login.html")


# 注册请求
@app.route('/validate/register',methods=['POST', 'GET'])
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        uemail = request.form['email']
        upsd = md5(request.form['password'])
        uname = request.form['username']
        USER = User(email=uemail, password=upsd, username=uname)
        db.session.add(USER)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html')

#邮箱格式校验
@app.route('/validate/<email>')
def validate_email(email):
    print("--", email, '--')
    if (email == 'NULL'):
        flash(u"请正确填写邮箱格式", 'info')
        email = ''
    else:
        try:
            email_2 = User.query.filter_by(email=email).first().email
        except AttributeError:
            flash(u'邮箱尚未注册', 'success')
        else:
            flash(u'邮箱已经被注册', 'warning')
            print(email_2)
    return render_template("register.html", var1=email)


@app.route('/button')
def button():
    return render_template('test/button.html')


if __name__ == '__main__':
    app.run()
