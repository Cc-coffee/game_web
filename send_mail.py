# #! usr/bin/python
# #coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。
#
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText
# from email.utils import parseaddr, formataddr
# import smtplib
#
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
#
# def strart_send(to_addr,code):
#     # 输入Email地址和口令:
#     from_addr = "********"
#     password = "********"
#     # 输入收件人地址:
#     # to_addr = "*******"
#     # 输入SMTP服务器地址:
#     smtp_server = "smtp.163.com"
#     text = "<pre> <h1>hello, Your Verify code is <h1> <br> <h2 style='color: red'>"+code+"</h2></pre>"
#     msg = MIMEText(text, 'html', 'utf-8')
#     msg['From'] = _format_addr('TankWord官方 <%s>' % from_addr)
#     msg['To'] = _format_addr('客户 <%s>' % to_addr)
#     msg['Subject'] = Header('验证码邮件', 'utf-8').encode()
#
#     server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
#     server.set_debuglevel(1)
#     server.login(from_addr, password)
#     server.sendmail(from_addr, [to_addr], msg.as_string())
#     server.quit()



# !/usr/bin/env python
# coding: utf-8

from flask_mail import Mail, Message
from threading import Thread
from config import *

mail = Mail(app)


## 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


# str转化为list
def str_To_list(str):
    x = str
    y = []
    y.append(x)
    return y


# 启动发送
def strart_send(recipients, code):
    msg = Message(subject='验证码邮件', sender="*******", recipients=str_To_list(recipients))
    #  msg.body = text_body
    msg.html = "<pre> <h1>hello, Your Verify code is <h1>  <h2 style='color: red'>" + code + "</h2></pre>"

    thread = Thread(target=send_async_email, args=[app, msg])
    thread.start()

    # mail.send(msg)

    return '<h1>邮件发送成功</h1>'
