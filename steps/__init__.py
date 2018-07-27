#!/usr/bin/env python
# -- coding=utf-8 --

"""
自定义预处理类型
"""

from behave import register_type

def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)


def parse_list(text):
    """
    Convert str into a List, seperated by ','
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: List instance (List), created from parsed text
    """
    return text.split(",")

def parse_dic(text):
    """
    Convert str into a Dictionary, seperated by ','
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Dictionary instance (Dictionary), created from parsed text
    """
    return eval(text)

# -- REGISTER: User-defined type converter (parse_type).
register_type(Number=parse_number)
register_type(List=parse_list)
register_type(Dic=parse_dic)