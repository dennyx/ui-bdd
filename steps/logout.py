
from behave import given
from behave import when
from behave import then
from utils.selenium_util import wait_for_element_show, FIND_ELEMENT_METHOD, wait_ajax_finish
from pages.head_page import HeadPage


@then('logout')
def do_logout(context):
    head_page = HeadPage(context)
    wait_ajax_finish(context.browser)
    head_page.set_base_element()
    head_page.logoutbtn.click()