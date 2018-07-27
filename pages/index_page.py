class IndexPage():

    def __init__(self, context):
        self.context = context


    def set_base_element(self):
        #退出
        self.logoutbtn = self.context.browser.find_element_by_id("logout")
        #收银台
        self.cashier = self.context.browser.find_element_by_xpath("//span[@class='cashier']/a")
        #修改密码
        self.mpassword = self.context.browser.find_element_by_xpath("//div[@class='container-login']/ul[@class='nav navbar-nav']/li[5]/span/a")
        #收款二维码
        self.qrCode = self.context.browser.find_element_by_xpath("//div[@class='pull-right']/a[@id='qrCode']")
        #刷新
        self.refresh = self.context.browser.find_element_by_id("refresh")


