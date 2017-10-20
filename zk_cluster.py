# encoding: utf-8
import socket
import config


class ZkServer(object):
    def __init__(self, conn_str):
        self.addrs = conn_str.split(',')

    # 获取该节点是否正常对外服务
    def ruok(self, ip, port):
        # 设置socket超时时间，网络不通时的测试时间
        socket.setdefaulttimeout(config.socket_time_out)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            s.connect((ip, port))
            s.send('ruok')
            return s.recv(1024)
        except socket.timeout as sto:
            return 'net_disConn'
        except socket.error as se:
            return 'IamDown'

    # 获取该节点的角色和连接数
    def srvrRole(self, ip, port):
        socket.setdefaulttimeout(2)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            s.connect((ip, port))
            s.send('srvr')
            result = s.recv(1024)
            if 'follower' in result:
                roleFlag = 'F'
            else:
                roleFlag = 'L'
            conns = result.split('\n')[4].split(':')[1]
            return roleFlag + ' |' + conns
        except socket.timeout as sto:
            return 'net_disConn'
        except socket.error as se:
            return 'IamDown'

    # 给前台展示
    def giveFront(self):
        result = []
        for addr in self.addrs:
            ip_port = addr.split(':')
            first = self.ruok(ip_port[0], int(ip_port[1]))
            second = self.srvrRole(ip_port[0], int(ip_port[1]))
            result.append(first + ' | ' + second)
        return result

# if __name__ == '__main__':
#     print ZkServer('172.21.11.63:8501,172.21.11.64:8501,172.21.11.65:8501').giveFront()
