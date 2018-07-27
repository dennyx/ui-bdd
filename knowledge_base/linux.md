# Linux相关储备

## 安装chrome浏览器

* 命令

```
yum install  \
    ipa-gothic-fonts \
    xorg-x11-fonts-100dpi \
    xorg-x11-fonts-75dpi \
    xorg-x11-utils \
    xorg-x11-fonts-cyrillic \
    xorg-x11-fonts-Type1 \
    xorg-x11-fonts-misc -y

yum install xorg-x11-server-Xvfb
echo "[google-chrome]" >> /etc/yum.repos.d/google-chrome.repo
echo "name=google-chrome" >> /etc/yum.repos.d/google-chrome.repo
echo "baseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch" >> /etc/yum.repos.d/google-chrome.repo
echo "enabled=1" >> /etc/yum.repos.d/google-chrome.repo
echo "gpgcheck=1" >> /etc/yum.repos.d/google-chrome.repo
echo "gpgkey=https://dl.google.com/linux/linux_signing_key.pub" >> /etc/yum.repos.d/google-chrome.repo
yum -y install google-chrome-stable

xvfb-run --server-args='-screen 0, 1024x768x16' google-chrome --headless --disable-gpu -remote-debugging-port=9222
```
* 参考 https://blog.ruhm.me/post/selenium-with-chrome-headless-on-centos-7/
