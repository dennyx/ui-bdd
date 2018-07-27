## Docker

### 简介

* 修改docker 仓库

### 为什么使用

* 跨平台
* 稳定性
* 并发

### 常用命令

```bash
# 查看docker本地镜像
docker images

# 查看当前活着的container
docker ps

# 查看所有container
docker ps -a

# 进入docker container中
docker exec -it 775c7c9ee1e1 /bin/bash 

# 复制文件到container中
docker cp image 775c7c9ee1e1:/image
```

### 搭建selenium环境

```bash
# 拉取selenium/hub镜像文件
docker pull selenium/hub
# 拉取selenium/node-firefox-debug镜像文件
docker pull selenium/node-firefox-debug
# 拉取selenium/node-chrome-debug镜像文件
docker pull selenium/node-chrome-debug
# 为镜像selenium/hub创建container实例
docker run -d -p 4444:4444 --name selenium_hub selenium/hub
# 为镜像selenium/hub创建container实例
docker run -d -p 5911:5900 --name selenium_chrome --link selenium_hub:hub --shm-size=512m selenium/node-chrome-debug
# 为镜像selenium/hub创建container实例
docker run -d -p 5917:5900 --name selenium_firefox --link selenium_hub:hub --shm-size=512m selenium/node-firefox-debug
```

* 打开浏览器，可以查看selenium console http://localhost:4444/grid/console?config=true&configDebug=true#


### ps

* 扩展工具 
    1. docker图形化管理工具 kitematic
    2. vnc viewer 客户端
* vnc密码secret，不需要指定用户名: 127.0.0.1:5917
* 如果发现请求chrome浏览器没有反应，则需要重启hub和对应的chrome的docker

