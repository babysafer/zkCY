# encoding: utf-8
from zk_cluster import  ZkServer
from werkzeug.security import generate_password_hash

i=generate_password_hash('Paas@2017')
print i

print ZkServer('172.21.11.63:8501,172.21.11.64:8501,172.21.11.65:8501').giveFront()
