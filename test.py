# encoding: utf-8

from werkzeug.security import generate_password_hash

i=generate_password_hash('Paas@2017')
print i