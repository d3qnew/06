#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/1 14:45
# @File    : Model.py
"""
数据模型

"""

from flask_login import UserMixin
from app import login_manger
from app import db


class Users(UserMixin, db.Model):
    __tablename__ = 'user'  # 对应mysql数据库表
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
