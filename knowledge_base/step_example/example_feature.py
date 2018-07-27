# -*- coding: UTF-8 -*-

from behave import given, when, then
import logging

@given('test user data')
def test_user(context):
    for row in context.table:
        logging.info("user.id as %s" % row['id'])
        logging.info("user.value as %s" % row['value'])