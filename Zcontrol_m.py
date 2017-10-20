# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, session
import config
from werkzeug.security import check_password_hash
from decorators import login_required
import zk_cluster

# todo title旁边的小图标

app = Flask(__name__)
app.config.from_object(config)



# 登录界面
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        USER_NAME_F = request.form.get('user_name')
        PASSWD = request.form.get('passwd')
        # 验证用户名、密码：
        if USER_NAME_F not in config.user_info.keys():
            return u'用户不存在'
        # elif PASSWD != config.user_info.get(USER_NAME_F):
        elif check_password_hash(config.user_info.get(USER_NAME_F), PASSWD):
            session['user_id'] = USER_NAME_F
            return redirect(url_for('home'))
        else:
            return u'密码不正确'


# 注册界面
@app.route('/create_account')
def create_account():
    return render_template('create_account.html')


# 主界面,login_required是before required 钩子函数
@app.route('/home')
@login_required
def home():
    # todo 待思考
    # f=[[]]
    # for key in config.conn_str.keys():
    #     ZkServer(config.conn_str[key]).giveFront()
    return render_template('home.html')

# 注销功能
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# 一个集群详细界面
@app.route('/detail')
@login_required
def deteil():
    return render_template('detail.html')


# 添加集群界面
@app.route('/addCluster')
@login_required
def addCluster():
    # todo 从前台传进来一个from然后更改现有的config文件中的一个字典
    # config.conn_str['北京测试2']='172.21.11.63:8541,172.21.11.64:8541,172.21.11.65:8541'
    # print config.conn_str
    return render_template('addCluster.html')


if __name__ == '__main__':
    app.run()
