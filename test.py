# encoding: utf-8
from zk_cluster import  ZkServer
from werkzeug.security import generate_password_hash

i=generate_password_hash('Paas@2017')
print i

centxt = '172.29.11.66:11001,172.21.11.67:11001,172.21.11.73:11001'
cent_tmp = centxt.split(',')
print cent_tmp

ip= cent_tmp[0].split(':')
print ip

