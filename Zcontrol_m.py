# encoding: utf-8
from flask import Flask, render_template, request, redirect, url_for, session
import config
from werkzeug.security import check_password_hash
from decorators import login_required
from zk_cluster import ZkServer, common, ifLeader

app = Flask(__name__)
app.config.from_object(config)


@app.route('/readme')
def readme():
    return render_template('readme.html')


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
            session.permanent = True
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
    zkResult = {}
    for zkClusterName in config.conn_str.keys():
        zkResult[zkClusterName] = ZkServer(config.conn_str[zkClusterName]).giveFront()

    # zkResult = {u'\u5317\u4eac\u6d4b\u8bd52': ['imok | F | 14', 'imok | L | 1', 'imok | F | 1'], u'\u5317\u4eac\u6d4b\u8bd5': ['imok | F | 1', 'imok | F | 1', 'imok | L | 1']}
    # for key, value in zkResult.iteritems():
    #     print key, ':', value
    return render_template('home.html', zkResult=zkResult)


# 注销功能
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# 一个集群详细界面
@app.route('/detail/<zkClusterName>')
@login_required
def detail(zkClusterName):
    # 获取集群的conn_str然后split成'172.29.11.66:11001'的list
    ip_port_List = config.conn_str[zkClusterName].split(',')
    conf = ''
    for ip_port in ip_port_List:
        if ifLeader(ip_port):
            conf = common(ip_port, 'conf')
            mntr = common(ip_port, 'mntr')
            dump = common(ip_port, 'dump')
            envi = common(ip_port, 'envi')
    if conf == '':
        conf = mntr = dump = envi = u'集群没有leader'
    return render_template("detail.html", conf=conf, mntr=mntr, dump=dump, envi=envi, zkClusterName=zkClusterName)


# 一个节点的详细信息
@app.route('/<zkClusterName>/<id>')
@login_required
def one(zkClusterName, id):
    ip_port_list = config.conn_str[zkClusterName].split(',')
    Iid = int(id)
    srvr = common(ip_port_list[Iid], 'srvr')
    conf = common(ip_port_list[Iid], 'conf')
    cons = common(ip_port_list[Iid], 'cons')
    dump = common(ip_port_list[Iid], 'dump')
    envi = common(ip_port_list[Iid], 'envi')
    stat = common(ip_port_list[Iid], 'stat')
    wchs = common(ip_port_list[Iid], 'wchs')

    return render_template('one.html', srvr=srvr, conf=conf, cons=cons, dump=dump, envi=envi, stat=stat, wchs=wchs,
                           ip_port=ip_port_list[Iid])


# 添加集群界面,下一个版本迭代吧
@app.route('/addCluster')
@login_required
def addCluster():
    # todo 从前台传进来一个from然后更改现有的config文件中的一个字典
    # config.conn_str['北京测试2']='172.21.11.63:8541,172.21.11.64:8541,172.21.11.65:8541'
    # print config.conn_str
    return render_template('addCluster.html')

# todo 添加把配置文件显示到前台的界面


if __name__ == '__main__':
    app.run()
