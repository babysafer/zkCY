# encoding:utf-8

from functools import wraps
from flask import session,redirect,url_for

# 装饰器，在所有函数执行前执行，渲染界面的时候有些需要判断是否已经登录
def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper

