# -*- coding: utf-8 -*-
# Author  : 李俊阳
# @Time    : 2019/9/3 22:24

import unittest
from classtest.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "调查你最喜欢的编程语言"
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses('python')
        self.assertIn('python', my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会不会被正确存储"""
        question = "调查你最喜欢的三门编程语言"
        my_survey = AnonymousSurvey(question)
        responses = ['python','java','c++']
        for response in responses:
            my_survey.store_responses(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()
