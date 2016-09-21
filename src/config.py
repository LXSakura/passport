# -*- coding:utf8 -*-

import os

#全局配置端
GLOBAL={

    "Host": os.environ.get("host", "0.0.0.0"),
    #Application run network address, you can set it `0.0.0.0`, `127.0.0.1`, ``;

    "Port": os.environ.get("port", 10030),
    #Application run port, default port;

    "Debug": os.environ.get("debug", True),
    #The development environment is open, the production environment is closed, which is also the default configuration.

    "LogLevel": os.environ.get("loglevel", "DEBUG"),
    #应用程序写日志级别，目前有DEBUG，INFO，WARNING，ERROR，CRITICAL

    "put2Redis": os.environ.get("put2redis", True),
    #是否开启put至redis的线程

    "ACL": ("Team.Front", "Team.Api"),
    #Access Control List, 访问控制列表, 限定只有ACL定义中的应用可以访问某些资源。

    "AppPrefix": "TeamAuth.Registered.Application",
    #应用注册信息写入集群的前缀名

}


#生产环境配置段
PRODUCT={

    "ProcessName": "Auth",
    #Custom process, you can see it with "ps aux|grep ProcessName".

    "ProductType": os.environ.get("producttype", "tornado"),
    #生产环境启动方法，可选`gevent`, `tornado`。
}


#模块配置项
MODULES={
    #指定应用会话存储集群，暂时支持redis、redis_cluster、etcd、memory(StringIO),
    "Session": os.environ.get("session", {
        "type": "redis_cluster",
        #会话存储集群类型
        "host": "101.200.125.9",
        #会话存储集群host/ip,
        "port": 10101,
        #会话存储集群port,
        "pass": None
        #验证密码(目前仅支持单实例版redis)
    }),

    #本地认证模块
    "Authentication": os.environ.get("authentication", {
        "type": "mysql",
        #认证来源, 支持mysql表、LDAP、
        "host": "101.200.125.9",

        "port": 3306,

        "pass": None
    }),

    #权限管理模块
    "Authority": os.environ.get("authority"),
}
