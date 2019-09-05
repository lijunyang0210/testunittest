# -*- coding: utf-8 -*-
# Author  : 李俊阳
# @Time    : 2019/9/3 22:01


class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_responses(self, new_response):
        """储存单份调查问卷的答案"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收集到的所有答案"""
        print('all results')
        for response in self.responses:
            print("--->" + response)
