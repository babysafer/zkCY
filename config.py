# encoding: utf-8
import os

DEBUG = True

#session 使用的secret key
SECRET_KEY = os.urandom(24)

# 登录用户名密码,01,Paas@2017,02,Paas@2018
user_info = {
    'paas01': 'pbkdf2:sha256:50000$UWhZQLmY$a5d82d19c3a3069e300a3fbdd75ef0eba87f54e44a7d76b179eef258e216d049',
    'paas02': 'pbkdf2:sha256:50000$FFGUSrnd$08a79f44fdc10b53d203512bddcd0ae8e4d2d14e45ea5e2e4fc10173f0817077'
}

# 目标zookeeper地址
conn_str = {
    '北京测试': '172.21.11.63:8501,172.21.11.64:8501,172.21.11.65:8501'
}

# socket超时时间
socket_time_out = 2
