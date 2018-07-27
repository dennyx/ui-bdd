# UI自动化


## 简介
* UI自动化，基于python + selenium + behave(BDD) + allure(报告)实现


## 基本框架

* selenium
* behave - python BDD实现， behave执行时，会读取当前目录下的behave.ini配置文件


## 项目运行依赖包
* pip install virtualenv
* pip install -r requirements.txt

* 主要步骤
    * 在当前目录下，建立一个虚拟环境，文件名为venv
    * virtualenv venv
    * 激活你的当前项目的虚拟环境
    * Windows: .\venv\Scripts\activate.pl1
    * 根据项目的requirements.txt文件，来安装对应的依赖，且固定版本
    * pip install -r requirements.txt
    * 导出项目的依赖，以方便别人使用
    * pip freeze > requirements.txt


## 前提条件

* 将res目录增加到windows PATH中，后续利用脚本来实现
```bash
behave -f allure_behave.formatter:AllureFormatter -o report ./features
```
* powershell 执行 Set-ExecutionPolicy RemoteSigned -scope CurrentUser
* powershell 执行 iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
* powershell 执行 scoop install allure
* chrome浏览器插件 xpath-helper


## 基本结构

* report/ allure_result/  临时报告目录
* download/ 临时下载目录
* features feature文件目录
* knowledge_base 知识储备
    * feature_example feature文件常用示例，作为学习参考库，便于快速定位
    * step_example step常用示例，作为学习参考库，便于快速定位
* pages 页面对象目录
* res 依赖工具目录
* steps 步骤定义文件目录
* utils 常用工具目录
* environment.py 世界文件
* config_template.py 配置模板，每个人根据自己的需求，复制一份config.py文件
* behave.ini behave基础配置文件


## 执行测试

* powershell 执行 behave -f allure_behave.formatter:AllureFormatter -o report ./features
* powershell 执行 allure generate report -o allure_report --clean
* powershell 执行 allure open allure_report
* 访问终端的链接，查看报告
* 查看日志 anhui_merchant.log
* ghostdriver.log 为使用phantom.js时，产生的日志


## behave常用命令

* 指定执行tag 
```bash
behave -f allure_behave.formatter:AllureFormatter -o report '.\features\LM Accounts Management\lm_account_opening.feature' -t DEBUG
```

* allure集成命令
```bash
allure serve report
```


## Git 提交步骤（同一个branch）

* 查看本地更新的代码
* commit需要提交的内容，到本地仓库
* git pull
* 查看其他人提交的内容
* 处理merge，如果存在的话
* 查看提交的内容
* git push


## TAG 标记

* NEED_LOGIN 需要登录
* EXAMPLE 示例代码，不要执行

## TODO

* 指定上传文件目录，上传文件到docker服务器中  -- 应该自动执行
* 注意事项，有需要用到pyautogui的，焦点应该在虚拟机中，否则会定位失败  -- 定位执行，其实还是在本地  -- 需要上传spy.py文件，用于控制在docker中的定位
* 考虑：是否将一整套，全部加到docker环境中？这样更加稳定，每人分布一个docker执行机器，连接到hub上；主要为了本地化的操作
* Docker服务器，时间调整, 浏览器乱码调整
* 运行前，需要清理session，否则会导致卡死 - 例如，强制关闭浏览器时的问题   -- 这个是运行出现异常时导致的问题
* 调整时间处理
* 可能存在网络问题 -- docker中，需要调整对应的参数
* 需要修改上传图片方式 -- 减少系统的依赖， pyautogui现在是在本机执行的，所以焦点在本机