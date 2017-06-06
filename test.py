# -*- coding: utf-8 -*-
from django.http import request
from flask_moment import Moment
from datetime import datetime
from flask import *
import re
from model import *
from flask_bootstrap import Bootstrap
from send_mail import *
from  rand import GenPassword

####################################################


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


# 校验邮箱格式
def validate_emails(e):
    if len(e) >= 5:
        if re.match("[a-zA-Z0-9]+\@+[a-zA-Z0-9]+\.+[a-zA-Z]", e) != None:
            # re.match(pattern, string) 尝试从字符串string的开始匹配一个模式。
            return None
    return True


# 校验密码格式
def validate_password(e):
    if len(e) >= 6 and len(e) <= 12:
        if re.match("[a-zA-Z]+[0-9]", e) != None:
            return None
    return True


# 全局变量验证码
verify_send = None


##################################################################


# 测试
@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('New_index/index.html', )


# 主页
@app.route('/')
def index():
    return render_template('New_index/index.html', )


# 自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# 用户中心
@app.route('/usercenter', methods=['POST', 'GET'])
def usercenter():
    if request.method == 'POST':
        nickname = request.form['nickname']
        signature = request.form['signature']
        gender = request.form['gender']
        birthday = request.form['birthday']
        purpose = request.form['purpose']
        try:
            a = User.query.filter_by(email=uemail_1).first()
            a.nickname = nickname
            a.signature = signature
            a.gender = gender
            a.birthday = birthday
            a.purpose = purpose
            db.session.add(a)
            db.session.commit()
            flash(u'修改成功', 'success')
        except:
            flash(u'修改失败', 'danger')
        finally:
            return render_template("usercenter.html", email=uemail_1, nickname=nickname, signature=signature,
                                   gender=gender, birthday=birthday, purpose=purpose)
    return render_template("usercenter.html", email=uemail_1)


# 修改密码
@app.route('/modifypwd', methods=['POST', 'GET'])
def modifypwd():
    if request.method == 'POST':
        upwd_1 = request.form['password_1']
        upwd_2 = request.form['password_2']
        if upwd_1 == upwd_2:
            if (validate_password(upwd_1)):
                flash(u'密码格式不符合以字母开头的6-12位的字母数字组合', 'danger')
            else:
                upwd_1 = md5(upwd_1)
                a = User.query.filter_by(email=uemail_1).first()
                a.password = upwd_1
                db.session.commit()
                flash(u'修改成功', 'success')
        else:
            flash(u'2次密码不一致', 'danger')
    return render_template("modifypwd.html", email=uemail_1)


# 登录请求
@app.route('/validate/login')
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            global uemail_1
            uemail_1 = request.form['email']
            uemail_2 = User.query.filter_by(email=uemail_1).first().email
            upsd_1 = md5(request.form['password'])
            upsd_2 = User.query.filter_by(email=uemail_1).first().password
        except:
            flash(u'用户名密码错', 'danger')
        else:
            if uemail_1 == uemail_2 and upsd_1 == upsd_2:
                nickname = User.query.filter_by(email=uemail_1).first().nickname
                return render_template('usercenter.html', email=uemail_1, nickname=nickname)
            else:
                flash(u'用户名密码错', 'danger')
    return render_template("login.html")


# 注册请求
@app.route('/validate/register', methods=['POST', 'GET'])
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        uemail = request.form['email']
        upwd = md5(request.form['password'])
        uname = request.form['nickname']
        uverify = request.form['verify']
        try:
            User.query.filter_by(email=uemail).first().email
        except AttributeError:
            global verify_send
            if uverify == verify_send:
                USER = User(email=uemail, password=upwd, nickname=uname)
                ACCOUNT = Account(email=uemail, password=upwd, nickname=uname)
                db.session.add(USER)
                db.session.add(ACCOUNT)
                db.session.commit()
                flash(u'注册成功', 'success')
                return redirect(url_for("login"))
            else:
                flash(u'验证码输入错误', 'danger')
            return render_template('register.html', var1=uemail, var2=uname, var3=upwd, var4=uverify)
        else:
            flash(u'邮箱已经被注册', 'warning')
            return render_template('register.html', var1=uemail, var2=uname, var3=upwd, var4=uverify)
    return render_template('register.html')


# 邮箱格式校验
@app.route('/validate/<email>')
def validate_email(email):
    if (validate_emails(email)):
        flash(u"请正确填写邮箱格式", 'info')
        if email == "NULL":
            email = ""
    else:
        try:
            email_2 = User.query.filter_by(email=email).first().email
        except AttributeError:
            flash(u'邮箱尚未注册', 'success')
        else:
            flash(u'邮箱已经被注册', 'warning')
    return render_template("register.html", var1=email)


# 发送邮件
@app.route('/send_mail', methods=['POST', 'GET'])
@app.route('/validate/send_mail', methods=['POST', 'GET'])
def Send_mail():
    if request.method == "POST":
        try:
            global verify_send
            verify_send = GenPassword(4)
            strart_send(request.form['email_address'], verify_send)
        except:
            return redirect(url_for("register"))
    return render_template('register.html', )


if __name__ == '__main__':
    app.run()
