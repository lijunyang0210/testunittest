# -*- coding: utf-8 -*-
# Author  : 李俊阳
# @Time    : 2019/9/3 21:15


def get_formatted_name(first, last, middle=''):
    """生成整洁名字"""
    if middle:
        full_name = first+' '+middle+' '+last
    else:
        full_name = first + ' ' + last
    return full_name.title()
