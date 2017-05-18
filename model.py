# -*- coding: utf-8 -*-
#数据库Model
from config import *


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(64), unique=False, index=True)
    password = db.Column(db.String(64), )
    email = db.Column(db.String(64),unique=True)

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(64), unique=False, index=True)
    password = db.Column(db.String(64), )
    email = db.Column(db.String(64), unique=True)

#
# if __name__ == '__main__':
#     pass
    # db.create_all()
    #
    #
    # #删除旧的表
    # db.drop_all()
    # db.create_all()
    # #插入数据
    #
    # user_john = User(username='john',password='123' )
    # user_john1 = User(username='john', password='123')
    # user_john2 = User(username='john', password='123')
    # user_john3 = User(username='john', password='123')
    # # 准备把对象写入数据库之前，先要将其添加到会话中，数据库会话db.session和Flask session对象没有关系，数据库会话也称事物
    # # db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
    # db.session.add(user_john)
    # db.session.add(user_john1)
    # db.session.add(user_john2)
    # db.session.add(user_john3)
    # # 提交会话到数据库
    # db.session.commit()
    # 修改roles名
    # admin_role.name = 'Administrator'
    # db.session.add(admin_role)
    # db.session.commit()
    # 删除数据库会话，从数据库中删除“Moderator”角色
    # db.session.delete(mod_role)
    # db.session.commit()
    # 注意删除，和插入更新一样，都是在数据库会话提交后执行
    # 查询
    # print(user_role)
    # print(User.query.filter_by(role=user_role).all())