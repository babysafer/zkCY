# encoding: utf-8
import socket
import config


# 给首页展示用的类
class ZkServer(object):
    def __init__(self, conn_str):
        self.addrs = conn_str.split(',')

    # 获取该节点是否正常对外服务
    def ruok(self, ip, port):
        # 设置socket超时时间，网络不通时的测试时间
        try:
            # socket.setdefaulttimeout(config.socket_time_out)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(config.socket_time_out)
            s.connect((ip, port))
            s.send('ruok')
            res= s.recv(1024)
            s.close()
            return res+' '
        except socket.timeout:
            return 'netDown'
        except socket.error:
            return 'ImDown'

    # 获取该节点的角色和连接数
    def srvrRole(self, ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(config.socket_time_out)
            s.connect((ip, port))
            s.send('srvr')
            result = s.recv(1024)
            s.close()
            if 'follower' in result:
                roleFlag = 'F'
            else:
                roleFlag = 'L'
            conns = result.split('\n')[4].split(':')[1]
            return ' '+roleFlag + ' | ' + conns

        except socket.timeout:
            return 'netDown'
        except socket.error:
            return 'ImDown'

    # 给前台展示
    def giveFront(self):
        result = []
        for addr in self.addrs:
            ip_port = addr.split(':')
            first = self.ruok(ip_port[0], int(ip_port[1]))
            second = self.srvrRole(ip_port[0], int(ip_port[1]))
            result.append(first + '|' + second)
        return result

        # 产生详细信息的类
        # class ZkServerDetail(object):
        #     def __init__(self, conn_str,cmd):
        #         self.addrs = conn_str.split(',')
        #         self.cmd = cmd

        # 随意接收四字命令


def common(ip_port, cmd):
    # ip_port='172.21.11.66:11001'
    ip=ip_port.split(':')[0]
    port=int(ip_port.split(':')[1])
    try:
        # socket.setdefaulttimeout(config.socket_time_out)
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(config.socket_time_out)
        s.connect((ip, port))
        s.send(cmd)
        result = s.recv(1024)
        s.close()
    except socket.timeout:
        return 'netDown'
    except socket.error:
        return 'ImDown'
    return result

def isLeader(ip_port):
    ip = ip_port.split(':')[0]
    port = int(ip_port.split(':')[1])
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(config.socket_time_out)
        s.connect((ip, port))
        s.send('srvr')
        result = s.recv(1024)
        s.close()
        if 'follower' in result:
            return False
        else:
            return True
    except socket.timeout:
        return False
    except socket.error:
        return False


if __name__ == '__main__':

    #     print ZkServer('172.29.11.63:8501,172.21.11.64:8501,172.21.11.65:8501').giveFront()
    # print ZkServerDetail('172.29.11.66:11001,172.21.11.67:11001,172.21.11.73:11001', 'stat').common()
    print common('172.21.11.66:11001', 'mntr')
