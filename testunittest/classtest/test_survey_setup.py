# -*- coding: utf-8 -*-
# Author  : 李俊阳
# @Time    : 2019/9/5 21:47

import unittest
from classtest.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self) -> None:
        """创建一组调查对象和一组答案，供使用的测试方法使用"""
        question = "调查你最喜欢的一门或者多门编程语言"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['python', 'java', 'c++']

    def test_store_single_response(self):
        """测试单个答案是否能安全的储存"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.responses)

    def test_store_three_responses(self):
        """测试多个答案是否能安全储存"""
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
