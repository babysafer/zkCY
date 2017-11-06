### 注册
    不提供在线注册功能，请联系paas维护人员获取登录口令
### Overiew
    所有集群节点当前状态的展示界面
    集群名字    节点1   节点2   节点3   ······
    "imok | L | 7"      表示该节点存活，是leader，连接数是17
    "ImDown | ImDown"   表示该节点异常
    "netDown | netDown" 表示该节点网络不通等网络异常
### 集群详细界面
    在Overiew页面点击集群名字，进到一个集群详细界面
### 详细页面zk信息解释
#### wchs
    列出服务器watches的简洁信息：连接总数、watching节点总数和watches总数
#### cons
    所有连接到这台服务器的客户端连接/会话的详细信息。包括“接受/发送”的包数量、session id 、操作延迟、最后的操作执行等信息
#### stat
    输出服务器的详细信息：接收/发送包数量、连接数、模式（leader/follower）、节点总数、延迟。 所有客户端的列表
#### srvr
    输出服务器的详细信息。zk版本、接收/发送包数量、连接数、模式（leader/follower）、节点总数
#### conf
    相关服务配置的详细信息。比如端口、zk数据及日志配置路径、最大连接数，session超时时间、serverId等
#### dump
    列出未经处理的会话和临时节点（只在leader上有效）
#### envi
    输出关于服务器的环境详细信息（不同于conf命令），比如host.name、java.version、java.home、user.dir=/data/zookeeper-3.4.6/bin之类信息
#### mntr
    列出集群的健康状态。包括“接受/发送”的包数量、操作延迟、当前服务模式（leader/follower）、节点总数、watch总数、临时节点总数
#### wchc
    通过session分组，列出watch的所有节点，它的输出是一个与 watch 相关的会话的节点列表。如果watches数量很大的话，将会产生很大的开销，会影响性能，小心使用
#### wchp
    通过路径分组，列出所有的 watch 的session id信息。它输出一个与 session 相关的路径。如果watches数量很大的话，将会产生很大的开销，会影响性能，小心使用
#### srst
    重置服务器的统计信息


    
    
    