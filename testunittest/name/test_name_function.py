# -*- coding: utf-8 -*-
# Author  : 李俊阳
# @Time    : 2019/9/3 21:29

import unittest
from name.name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name.function.py"""

    def test_first_last_name(self):
        """能否正确处理Janis joplin这样的姓名"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能否正确处理li jun yang 这样的姓名"""
        formatted_name = get_formatted_name('li', 'yang', 'jun')
        self.assertEqual(formatted_name, 'Li Jun Yang')


if __name__ == '__main__':
    unittest.main()
