from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def strart_send(to_addr,code):
    # 输入Email地址和口令:
    from_addr = "tiancheng8096836@163.com"
    password = "HTC940122"
    # 输入收件人地址:
    # to_addr = "809683605@qq.com"
    # 输入SMTP服务器地址:
    smtp_server = "smtp.163.com"
    text = "hello, Your Verify code is "+code
    msg = MIMEText(text, 'plain', 'utf-8')
    msg['From'] = _format_addr('TankWord官方 <%s>' % from_addr)
    msg['To'] = _format_addr('客户 <%s>' % to_addr)
    msg['Subject'] = Header('验证码邮件', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
