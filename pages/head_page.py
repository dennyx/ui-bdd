class HeadPage():
    def __init__(self, context):
        self.context = context
        self.cashier_xpath = "//li[1]/span[@class='cashier']/a"

    def set_base_element(self):
        #收银台
        self.cashier = self.context.browser.find_element_by_xpath("//li[1]/span[@class='cashier']/a")
        self.mpassword = self.context.browser.find_element_by_xpath("//ul[@class='nav navbar-nav']/li[5]/span/a")
        self.logoutbtn = self.context.browser.find_element_by_id("logout")

        # self.logout = self.context.browser.find_element_by_id("logout")