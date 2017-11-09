# encoding: utf-8
from werkzeug.security import generate_password_hash
import sys

# python generationPassWD.py yourPaasWD 将生成的密码和用户名 配置
# 到config.py 的user_info字典中


if __name__ == '__main__':
    print    generate_password_hash(sys.argv[1])
