# 常见错误记录

# stale element reference

* 原因： 因页面刷新，导致元素找不到
* 错误trace： selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
* 解决方法： 重新获取一次元素

