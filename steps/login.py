from behave import given
from behave import when
from behave import then
import logging
from pages.login_page import LoginPage
from utils.selenium_util import wait_for_element_show, FIND_ELEMENT_METHOD, wait_ajax_finish
from pages.index_page import IndexPage

@given('login with "{username}" and "{password}"')
def do_login(context, username, password):
    context.curent_page = LoginPage(context)
    wait_for_element_show(context.browser, FIND_ELEMENT_METHOD.ID, context.curent_page.username_id)
    context.curent_page.set_base_element()
    context.curent_page.userNameInput.send_keys(username)
    context.curent_page.passwordInput.send_keys(password)
    context.curent_page.button.click()
    wait_ajax_finish(context.browser)
