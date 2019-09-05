# -*- coding: utf-8 -*-
# Author  : 李俊阳
# @Time    : 2019/9/3 22:12

from classtest.survey import AnonymousSurvey


question = "调查你最喜欢的编程语言"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("enter 'q'at any time to quit")
while 1==1:
    response = input('输入你最喜欢的编程语言:')
    if response == 'q':
        break
    my_survey.store_responses(response)

print('\n显示调查结果')
my_survey.show_results()