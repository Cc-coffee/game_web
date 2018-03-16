# -*- coding: utf-8 -*-
#配置数据库
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)


#数据库配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/battleworld?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


#flask_mail配置
app.config['DEBUG'] = False

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = '*******'
app.config['MAIL_PASSWORD'] = '******'


app.config['SECRET_KEY'] = 'hard to guess string'
